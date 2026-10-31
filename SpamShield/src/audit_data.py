
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "processed" / "emails.csv"
REPORT_DIR = PROJECT_DIR / "reports" / "results"
REPORT_FILE = REPORT_DIR / "data_audit.csv"


def load_dataset():
    """Carga el corpus de correos SpamAssassin."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"No se encontró el dataset: {DATA_FILE}\n"
            "Ejecuta primero: python src/prepare_data.py"
        )

    df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

    required_columns = {"message", "label", "source_archive"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Faltan columnas obligatorias: {sorted(missing_columns)}"
        )

    return df


def main():
    df = load_dataset()

    print("\n--- DATASET AUDITADO ---")
    print(DATA_FILE)

    print("\n--- DIMENSIONES ---")
    print(f"Filas: {len(df)}")
    print(f"Columnas: {len(df.columns)}")

    print("\n--- PRIMEROS MENSAJES ---")
    print(df[["label", "message"]].head(3).to_string(index=False))

    print("\n--- DISTRIBUCIÓN DE ETIQUETAS ---")
    print(df["label"].value_counts(dropna=False))

    print("\n--- VALORES FALTANTES ---")
    print(df[["message", "label", "source_archive"]].isna().sum())

    print("\n--- MENSAJES VACÍOS ---")
    empty_messages = (
        df["message"].fillna("").astype(str).str.strip().eq("")
    )
    print(f"Mensajes vacíos: {int(empty_messages.sum())}")

    print("\n--- DUPLICADOS EXACTOS ---")
    print(f"Filas duplicadas completas: {int(df.duplicated().sum())}")
    print(
        "Mensajes repetidos, sin importar la etiqueta: "
        f"{int(df.duplicated(subset=['message']).sum())}"
    )

    print("\n--- MENSAJES CON ETIQUETAS CONTRADICTORIAS ---")
    labels_per_message = df.groupby("message")["label"].nunique()
    conflicting = labels_per_message[labels_per_message > 1]
    print(f"Textos con más de una etiqueta: {len(conflicting)}")

    print("\n--- ETIQUETAS ENCONTRADAS ---")
    print(sorted(df["label"].dropna().unique()))

    print("\n--- REGISTROS POR ARCHIVO DE ORIGEN ---")
    print(
        df.groupby(["source_archive", "label"], dropna=False)
        .size()
        .to_string()
    )

    print("\n--- LONGITUD DE LOS MENSAJES ---")
    lengths = df["message"].fillna("").astype(str).str.len()
    print(lengths.describe().round(2).to_string())

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    audit = pd.DataFrame(
        [
            {"indicador": "total_filas", "valor": len(df)},
            {"indicador": "total_columnas", "valor": len(df.columns)},
            {
                "indicador": "valores_faltantes_totales",
                "valor": int(df.isna().sum().sum()),
            },
            {
                "indicador": "mensajes_vacios",
                "valor": int(empty_messages.sum()),
            },
            {
                "indicador": "filas_duplicadas_completas",
                "valor": int(df.duplicated().sum()),
            },
            {
                "indicador": "mensajes_repetidos",
                "valor": int(df.duplicated(subset=["message"]).sum()),
            },
            {
                "indicador": "textos_con_etiquetas_contradictorias",
                "valor": len(conflicting),
            },
        ]
    )

    audit.to_csv(REPORT_FILE, index=False, encoding="utf-8-sig")

    print(f"\nInforme guardado en: {REPORT_FILE}")


if __name__ == "__main__":
    main()
