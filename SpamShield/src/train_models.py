
from pathlib import Path
from time import perf_counter
import json

import joblib
import pandas as pd

from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    auc,
    average_precision_score,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = PROJECT_DIR / "data" / "processed" / "emails_clean.csv"
MODELS_DIR = PROJECT_DIR / "models"
RESULTS_DIR = PROJECT_DIR / "reports" / "results"

RANDOM_STATE = 42
TEST_SIZE = 0.20
POSITIVE_LABEL = "spam"


def load_data():
    """Carga y valida los datos limpios."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            "No existe emails_clean.csv. "
            "Ejecuta primero: python src/clean_data.py"
        )

    df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

    required = {"message", "label"}
    if not required.issubset(df.columns):
        raise ValueError(
            f"Faltan columnas: {required - set(df.columns)}"
        )

    df = df.dropna(subset=["message", "label"]).copy()
    df["message"] = df["message"].astype(str).str.strip()
    df["label"] = df["label"].astype(str).str.strip().str.lower()
    df = df[df["message"].ne("")]

    if not set(df["label"].unique()).issubset({"ham", "spam"}):
        raise ValueError("Se encontraron etiquetas no reconocidas.")

    # Evitamos textos repetidos en el conjunto limpio.
    if df["message"].duplicated().any():
        raise ValueError(
            "Hay mensajes repetidos. Ejecuta la limpieza nuevamente."
        )

    return df.reset_index(drop=True)


def build_models():
    """Define un baseline y dos clasificadores de texto."""
    return {
        "baseline": DummyClassifier(strategy="most_frequent"),

        "naive_bayes": Pipeline([
            ("tfidf", TfidfVectorizer(
                lowercase=True,
                strip_accents="unicode",
                ngram_range=(1, 2),
                max_features=50000,
                sublinear_tf=True,
            )),
            ("model", MultinomialNB(alpha=0.5)),
        ]),

        "logistic_regression": Pipeline([
            ("tfidf", TfidfVectorizer(
                lowercase=True,
                strip_accents="unicode",
                ngram_range=(1, 2),
                max_features=50000,
                sublinear_tf=True,
            )),
            ("model", LogisticRegression(
                max_iter=1000,
                class_weight=None,
                random_state=RANDOM_STATE,
            )),
        ]),
    }


def evaluate_model(name, model, X_train, X_test, y_train, y_test):
    """Entrena y calcula métricas dando prioridad a la clase spam."""

    start = perf_counter()
    model.fit(X_train, y_train)
    train_seconds = perf_counter() - start

    start = perf_counter()
    predictions = model.predict(X_test)
    inference_seconds = perf_counter() - start

    # Las métricas de ranking requieren puntuaciones de spam.
    average_precision = None
    pr_auc_trapezoidal = None

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X_test)
        classes = list(model.classes_)
        spam_index = classes.index(POSITIVE_LABEL)
        spam_probabilities = probabilities[:, spam_index]

        y_test_binary = (
            pd.Series(y_test).to_numpy() == POSITIVE_LABEL
        ).astype(int)

        # Average Precision (AP).
        average_precision = average_precision_score(
            y_test_binary,
            spam_probabilities,
        )

        # Área trapezoidal bajo la curva Precision-Recall.
        precision_curve, recall_curve, _ = precision_recall_curve(
            y_test_binary,
            spam_probabilities,
        )

        pr_auc_trapezoidal = auc(
            recall_curve,
            precision_curve,
        )

    matrix = confusion_matrix(
        y_test,
        predictions,
        labels=["ham", "spam"],
    )

    tn, fp, fn, tp = matrix.ravel()

    result = {
        "model": name,
        "accuracy": accuracy_score(y_test, predictions),
        "f1_macro": f1_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),
        "precision_spam": precision_score(
            y_test,
            predictions,
            pos_label=POSITIVE_LABEL,
            zero_division=0,
        ),
        "recall_spam": recall_score(
            y_test,
            predictions,
            pos_label=POSITIVE_LABEL,
            zero_division=0,
        ),
        
        "average_precision": average_precision,
        "pr_auc_average_precision": average_precision,
        "pr_auc_trapezoidal": pr_auc_trapezoidal,
        "true_negatives": int(tn),
        "false_positives": int(fp),
        "false_negatives": int(fn),
        "true_positives": int(tp),
        "train_seconds": train_seconds,
        "inference_ms_total": inference_seconds * 1000,
        "inference_ms_per_message": (
            inference_seconds * 1000 / len(X_test)
        ),
    }

    return result


def main():
    """Entrena los modelos y guarda resultados reproducibles."""

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    df = load_data()

    X = df["message"]
    y = df["label"]

    # Separación estratificada; el test no participa en el entrenamiento.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    print("--- PARTICIÓN ---")
    print(f"Total: {len(df)}")
    print(f"Entrenamiento: {len(X_train)}")
    print(f"Prueba: {len(X_test)}")
    print("\nDistribución en entrenamiento:")
    print(y_train.value_counts())
    print("\nDistribución en prueba:")
    print(y_test.value_counts())

    results = []
    models = build_models()

    for name, model in models.items():
        print(f"\nEntrenando {name}...")

        result = evaluate_model(
            name, model, X_train, X_test, y_train, y_test
        )
        results.append(result)

        # Guardar el modelo para la demostración.
        joblib.dump(model, MODELS_DIR / f"{name}.joblib")

        print(
            f"Precisión spam: {result['precision_spam']:.4f} | "
            f"Recall spam: {result['recall_spam']:.4f} | "
            f"F1 Macro: {result['f1_macro']:.4f}"
        )

    results_df = pd.DataFrame(results)
    results_file = RESULTS_DIR / "model_comparison.csv"

    results_df.to_csv(
        results_file,
        index=False,
        encoding="utf-8-sig",
    )

    split_info = {
        "dataset": "SpamAssassin Public Corpus",
        "clean_rows": len(df),
        "train_rows": len(X_train),
        "test_rows": len(X_test),
        "test_size": TEST_SIZE,
        "random_state": RANDOM_STATE,
        "stratified": True,
        "positive_label": POSITIVE_LABEL,
        "models": list(models.keys()),
    }

    with (RESULTS_DIR / "split_config.json").open(
        "w", encoding="utf-8"
    ) as file:
        json.dump(
            split_info,
            file,
            indent=2,
            ensure_ascii=False,
        )

  
    print("\n--- COMPARACIÓN FINAL ---")
    print(
        results_df[
            [
                "model",
                "precision_spam",
                "recall_spam",
                "average_precision",
                "pr_auc_trapezoidal",
                "f1_macro",
                "train_seconds",
            ]
        ].round(4).to_string(index=False)
    )



if __name__ == "__main__":
    main()
