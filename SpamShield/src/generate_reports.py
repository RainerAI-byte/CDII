from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    ConfusionMatrixDisplay,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

from train_models import load_data, RANDOM_STATE, TEST_SIZE


PROJECT_DIR = Path(__file__).resolve().parents[1]
MODELS_DIR = PROJECT_DIR / "models"
RESULTS_DIR = PROJECT_DIR / "reports" / "results"
FIGURES_DIR = PROJECT_DIR / "reports" / "figures"

LABELS = ["ham", "spam"]


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    # Reconstruir exactamente la partición experimental original.
    df = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        df["message"],
        df["label"],
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=df["label"],
    )

    print(f"Correos de prueba: {len(X_test)}")

    metric_rows = []
    matrix_rows = []

    model_names = [
        "baseline",
        "naive_bayes",
        "logistic_regression",
    ]

    fig, axes = plt.subplots(
        1, 3, figsize=(15, 4.8), constrained_layout=True
    )

    for name, ax in zip(model_names, axes):
        model_path = MODELS_DIR / f"{name}.joblib"

        if not model_path.exists():
            raise FileNotFoundError(
                f"No se encontró el modelo: {model_path}"
            )

        model = joblib.load(model_path)
        predictions = model.predict(X_test)

        # Matriz: filas = clase real; columnas = clase predicha.
        matrix = confusion_matrix(
            y_test, predictions, labels=LABELS
        )

        tn, fp, fn, tp = matrix.ravel()

        ConfusionMatrixDisplay(
            confusion_matrix=matrix,
            display_labels=LABELS,
        ).plot(
            ax=ax,
            cmap="Blues",
            colorbar=False,
            values_format="d",
        )

        ax.set_title(name.replace("_", " ").title())

        matrix_rows.append({
            "model": name,
            "true_negatives": int(tn),
            "false_positives": int(fp),
            "false_negatives": int(fn),
            "true_positives": int(tp),
        })

        metric_rows.append({
            "model": name,
            "accuracy": accuracy_score(y_test, predictions),
            "f1_macro": f1_score(
                y_test, predictions, average="macro",
                zero_division=0,
            ),
            "precision_spam": precision_score(
                y_test, predictions, pos_label="spam",
                zero_division=0,
            ),
            "recall_spam": recall_score(
                y_test, predictions, pos_label="spam",
                zero_division=0,
            ),
        })

        print(
            f"{name}: TN={tn}, FP={fp}, "
            f"FN={fn}, TP={tp}"
        )

    fig.suptitle(
        "SpamShield — Matrices de confusión",
        fontsize=14,
    )

    figure_path = FIGURES_DIR / "confusion_matrices.png"
    fig.savefig(figure_path, dpi=180, bbox_inches="tight")
    plt.close(fig)

    pd.DataFrame(matrix_rows).to_csv(
        RESULTS_DIR / "confusion_matrices.csv",
        index=False,
        encoding="utf-8-sig",
    )

    pd.DataFrame(metric_rows).to_csv(
        RESULTS_DIR / "recomputed_metrics.csv",
        index=False,
        encoding="utf-8-sig",
    )

    print("\nArchivos generados:")
    print(figure_path)
    print(RESULTS_DIR / "confusion_matrices.csv")
    print(RESULTS_DIR / "recomputed_metrics.csv")


if __name__ == "__main__":
    main()