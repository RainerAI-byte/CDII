
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = PROJECT_DIR / "data" / "processed" / "emails.csv"
OUTPUT_FILE = (
    PROJECT_DIR / "data" / "processed" / "emails_clean.csv"
)


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo original: {INPUT_FILE}"
        )

    df = pd.read_csv(INPUT_FILE, encoding="utf-8-sig")

    required_columns = {"message", "label", "source_archive"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Faltan columnas: {sorted(missing_columns)}"
        )

    original_rows = len(df)

    # Eliminamos filas sin texto o sin etiqueta.
    df = df.dropna(subset=["message", "label"]).copy()
    df["message"] = df["message"].astype(str).str.strip()
    df["label"] = df["label"].astype(str).str.strip()

    df = df[df["message"].ne("")].copy()

    # Evitamos que un mensaje exacto aparezca varias veces.
    # Conservamos la primera aparición y su archivo de origen.
    df = df.drop_duplicates(
        subset=["message"],
        keep="first",
    ).reset_index(drop=True)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig",
    )

    print("\n--- LIMPIEZA COMPLETADA ---")
    print(f"Filas originales: {original_rows}")
    print(f"Filas después de limpiar: {len(df)}")
    print(f"Filas eliminadas: {original_rows - len(df)}")

    print("\n--- DISTRIBUCIÓN FINAL ---")
    print(df["label"].value_counts())

    print("\n--- PORCENTAJE POR CLASE ---")
    print(
        (df["label"].value_counts(normalize=True) * 100)
        .round(2)
        .astype(str)
        .add("%")
    )

    print(f"\nArchivo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
