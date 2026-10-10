
from __future__ import annotations

import argparse
import json
from time import perf_counter

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity

from inf8239_u03.config import MOVIELENS_DIR, ROOT
from inf8239_u03.data import load_movielens
from inf8239_u03.metrics import catalog_coverage, hit_rate_at_k
from inf8239_u03.recommenders import MatrixFactorization, temporal_leave_one_out


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluación de recomendación híbrida para INF-8239 LAB09."
    )
    parser.add_argument("--factors", type=int, default=20)
    parser.add_argument("--epochs", type=int, default=12)
    parser.add_argument("--alpha", type=float, default=0.75)

    args = parser.parse_args()

    if args.factors < 1:
        parser.error("--factors debe ser mayor que cero.")

    if args.epochs < 1:
        parser.error("--epochs debe ser mayor que cero.")

    if not 0.0 <= args.alpha <= 1.0:
        parser.error("--alpha debe estar entre 0 y 1.")

    # 1. Cargar datos y realizar la partición temporal.
    ratings, movies = load_movielens(MOVIELENS_DIR)
    train, test = temporal_leave_one_out(ratings)

    # 2. Entrenar el modelo de factorización matricial.
    start = perf_counter()

    model = MatrixFactorization(
        factors=args.factors
    ).fit(
        train,
        epochs=args.epochs,
    )

    train_seconds = perf_counter() - start

    # 3. Evaluar RMSE únicamente para usuarios e ítems conocidos.
    evaluable = test[
        test["userId"].isin(model.user_index)
        & test["movieId"].isin(model.item_index)
    ].copy()

    if evaluable.empty:
        raise ValueError(
            "No hay observaciones de prueba evaluables para calcular RMSE."
        )

    predictions = [
        model.predict(row.userId, row.movieId)
        for row in evaluable.itertuples()
    ]

    rmse = root_mean_squared_error(
        evaluable["rating"],
        predictions,
    )

    # 4. Construir la matriz de géneros para el recomendador híbrido.
    movie_table = movies.reset_index(drop=True).copy()

    movie_table["genres_text"] = (
        movie_table["genres"]
        .fillna("")
        .str.replace("|", " ", regex=False)
    )

    vectorizer = TfidfVectorizer()
    genre_matrix = vectorizer.fit_transform(
        movie_table["genres_text"]
    )

    movie_row = {
        int(movie_id): index
        for index, movie_id in enumerate(movie_table["movieId"])
    }

    # 5. Calcular popularidad como alternativa para cold start.
    popular = (
        train.groupby("movieId")["rating"]
        .agg(["mean", "count"])
        .sort_values(
            ["count", "mean"],
            ascending=False,
        )
    )

    popular_items = popular.index.tolist()

    # 6. Generar recomendaciones híbridas por usuario.
    recommendations = {}

    for user_id in evaluable["userId"].unique():
        seen = set(
            train.loc[
                train["userId"].eq(user_id),
                "movieId",
            ]
        )

        collaborative = model.top_n(
            user_id,
            seen,
            100,
        )

        if collaborative.empty:
            recommendations[int(user_id)] = []
            continue

        # Normalizar las puntuaciones colaborativas.
        collab_scores = collaborative["collaborative_score"]

        collab_min = collab_scores.min()
        collab_max = collab_scores.max()

        collaborative["normalized"] = (
            (collab_scores - collab_min)
            / max(collab_max - collab_min, 1e-9)
        )

        # Construir el perfil de géneros usando el historial del usuario.
        history = train.loc[
            train["userId"].eq(user_id)
            & train["movieId"].isin(movie_row),
            ["movieId", "rating"],
        ]

        history_rows = [
            movie_row[int(item)]
            for item in history["movieId"]
        ]

        if history_rows:
            weights = np.clip(
                history["rating"].to_numpy(dtype=float) - 2.5,
                0.1,
                None,
            )

            profile = (
                genre_matrix[history_rows]
                .multiply(weights[:, None])
                .sum(axis=0)
            )

            # Convertir a un arreglo NumPy 2D compatible con sklearn.
            profile = np.asarray(profile).reshape(1, -1)

            candidate_rows = [
                movie_row[int(item)]
                for item in collaborative["movieId"]
                if int(item) in movie_row
            ]

            # Alinear los candidatos con las filas disponibles en la matriz.
            candidate_ids = [
                int(item)
                for item in collaborative["movieId"]
                if int(item) in movie_row
            ]

            if candidate_rows:
                content_scores = cosine_similarity(
                    profile,
                    genre_matrix[candidate_rows],
                ).ravel()

                content_min = content_scores.min()
                content_max = content_scores.max()

                content_normalized = (
                    (content_scores - content_min)
                    / max(content_max - content_min, 1e-9)
                )

                content_by_id = dict(
                    zip(candidate_ids, content_normalized)
                )

                collaborative["content_score"] = (
                    collaborative["movieId"]
                    .map(content_by_id)
                    .fillna(0.0)
                )
            else:
                collaborative["content_score"] = 0.0

        else:
            # Si el usuario no tiene historial disponible, se usa solo
            # el componente colaborativo.
            collaborative["content_score"] = 0.0

        # 7. Combinar las puntuaciones.
        collaborative["hybrid_score"] = (
            args.alpha * collaborative["normalized"]
            + (1.0 - args.alpha) * collaborative["content_score"]
        )

        recommendations[int(user_id)] = (
            collaborative.nlargest(10, "hybrid_score")["movieId"]
            .astype(int)
            .tolist()
        )

    # 8. Calcular métricas.
    metrics = {
        "rmse": float(rmse),
        "hit_rate_at_10": float(
            hit_rate_at_k(recommendations, evaluable, 10)
        ),
        "catalog_coverage": float(
            catalog_coverage(recommendations, len(model.items))
        ),
        "train_seconds": float(train_seconds),
        "factors": int(args.factors),
        "epochs": int(args.epochs),
        "alpha": float(args.alpha),
        "cold_start_policy": (
            "Popularidad por cantidad de valoraciones y media; "
            "no personalizada"
        ),
    }

    # 9. Guardar las evidencias.
    reports_dir = ROOT / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    metrics_path = reports_dir / "hybrid_metrics.json"
    metrics_path.write_text(
        json.dumps(metrics, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    cold_start_items = popular_items[:10]

    cold_start = (
        movies[movies["movieId"].isin(cold_start_items)]
        .set_index("movieId")
        .reindex(cold_start_items)
        .reset_index()
    )

    cold_start.to_csv(
        reports_dir / "cold_start_fallback.csv",
        index=False,
    )

    print(json.dumps(metrics, indent=2, ensure_ascii=False))
    print(f"\nMétricas guardadas en: {metrics_path}")
    print(
        "Recomendaciones de fallback guardadas en: "
        f"{reports_dir / 'cold_start_fallback.csv'}"
    )


if __name__ == "__main__":
    main()