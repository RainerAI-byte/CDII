from __future__ import annotations

import json
from time import perf_counter

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity

from inf8239_u03.config import MOVIELENS_DIR, ROOT
from inf8239_u03.data import load_movielens
from inf8239_u03.metrics import catalog_coverage, hit_rate_at_k
from inf8239_u03.recommenders import MatrixFactorization, temporal_leave_one_out

ratings, movies = load_movielens(MOVIELENS_DIR)
train, test = temporal_leave_one_out(ratings)

# Una sola factorizacion para todos los metodos comparados.
start = perf_counter()
model = MatrixFactorization(factors=20).fit(train, epochs=12)
mf_seconds = perf_counter() - start

evaluable = test[
    test["userId"].isin(model.user_index)
    & test["movieId"].isin(model.item_index)
].copy()

predictions = [
    model.predict(row.userId, row.movieId)
    for row in evaluable.itertuples()
]
rmse = float(root_mean_squared_error(evaluable["rating"], predictions))

# Baseline de popularidad: cantidad de valoraciones y promedio.
start = perf_counter()
pop_table = train.groupby("movieId")["rating"].agg(["mean", "count"])
pop_order = pop_table.sort_values(
    ["count", "mean"], ascending=False
).index.tolist()
pop_seconds = perf_counter() - start

# Representacion de contenido mediante generos.
start = perf_counter()
movie_table = movies.reset_index(drop=True).copy()
movie_table["genres_text"] = movie_table["genres"].str.replace(
    "|", " ", regex=False
)
genre_matrix = TfidfVectorizer().fit_transform(movie_table["genres_text"])
movie_row = {
    int(movie_id): idx
    for idx, movie_id in enumerate(movie_table["movieId"])
}
content_seconds = perf_counter() - start

pop_recs = {}
content_recs = {}
factor_recs = {}
hybrid_recs = {}

for user_id in evaluable["userId"].unique():
    history = train.loc[train["userId"].eq(user_id)]
    seen = set(history["movieId"].astype(int))

    # Popularidad, excluyendo peliculas ya vistas.
    pop_recs[int(user_id)] = [
        int(mid) for mid in pop_order if int(mid) not in seen
    ][:10]

    # Perfil del usuario basado en generos de su historial.
    user_history = history[
        history["movieId"].isin(movie_row)
    ][["movieId", "rating"]]

    history_rows = [
        movie_row[int(mid)] for mid in user_history["movieId"]
    ]
    weights = np.clip(
        user_history["rating"].to_numpy() - 2.5, 0.1, None
    )

    if history_rows:
        profile = (
            genre_matrix[history_rows].multiply(weights[:, None]).sum(axis=0)
            / weights.sum()
        )
        candidates = [
            int(mid) for mid in movie_table["movieId"]
            if int(mid) not in seen
        ]
        candidate_rows = [movie_row[mid] for mid in candidates]
        scores = cosine_similarity(
            np.asarray(profile), genre_matrix[candidate_rows]
        ).ravel()
        best = np.argsort(scores)[::-1][:10]
        content_recs[int(user_id)] = [candidates[i] for i in best]
    else:
        content_recs[int(user_id)] = pop_recs[int(user_id)]

    # Ranking colaborativo por factorizacion.
    collaborative = model.top_n(int(user_id), seen, 100)
    factor_recs[int(user_id)] = (
        collaborative.nlargest(10, "collaborative_score")["movieId"]
        .astype(int).tolist()
    )

    # Hibrido: factorizacion y similitud de contenido.
    if len(collaborative):
        collaborative = collaborative.copy()
        scores = collaborative["collaborative_score"].to_numpy()
        span = scores.max() - scores.min()
        collaborative["normalized"] = (
            (scores - scores.min()) / max(span, 1e-9)
        )
        valid = collaborative["movieId"].astype(int).isin(movie_row)
        collaborative = collaborative.loc[valid].copy()
        candidate_ids = collaborative["movieId"].astype(int).tolist()
        candidate_rows = [movie_row[mid] for mid in candidate_ids]

        if history_rows and candidate_rows:
            cs = cosine_similarity(
                np.asarray(profile), genre_matrix[candidate_rows]
            ).ravel()
            cspan = cs.max() - cs.min()
            collaborative["content_score"] = (
                (cs - cs.min()) / max(cspan, 1e-9)
            )
        else:
            collaborative["content_score"] = 0.0

        collaborative["hybrid_score"] = (
            0.75 * collaborative["normalized"]
            + 0.25 * collaborative["content_score"]
        )
        hybrid_recs[int(user_id)] = (
            collaborative.nlargest(10, "hybrid_score")["movieId"]
            .astype(int).tolist()
        )
    else:
        hybrid_recs[int(user_id)] = pop_recs[int(user_id)]

def ranking_metrics(recs):
    return {
        "hit_rate_at_10": float(hit_rate_at_k(recs, evaluable, 10)),
        "catalog_coverage": float(
            catalog_coverage(recs, len(model.items))
        ),
    }

results = []
for name, recs, prep_seconds in [
    ("Popularidad", pop_recs, pop_seconds),
    ("Contenido", content_recs, content_seconds),
    ("Factorizacion", factor_recs, mf_seconds),
    ("Hibrido", hybrid_recs, mf_seconds + content_seconds),
]:
    row = {
        "method": name,
        **ranking_metrics(recs),
        "preparation_or_fit_seconds": float(prep_seconds),
        "rmse": rmse if name in ("Factorizacion", "Hibrido") else None,
    }
    results.append(row)

out = ROOT / "reports"
out.mkdir(exist_ok=True)
pd.DataFrame(results).to_csv(
    out / "comparison_metrics.csv", index=False
)
(out / "comparison_metrics.json").write_text(
    json.dumps(results, indent=2), encoding="utf-8"
)

print(pd.DataFrame(results).to_string(index=False))
print("\nGuardado: reports/comparison_metrics.csv")
print("Guardado: reports/comparison_metrics.json")
print(
    "\nNota: el RMSE corresponde a las predicciones de factorizacion. "
    "El hibrido cambia el ranking, no la prediccion de valoraciones."
)
