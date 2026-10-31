
from pathlib import Path
from email import policy
from email.parser import BytesParser
from email.header import decode_header, make_header
from email.message import Message
from io import StringIO
import csv
import tarfile

PROJECT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "emails.csv"

# El nombre del archivo determina la etiqueta.
ARCHIVES = {
    "20030228_easy_ham.tar.bz2": "ham",
    "20030228_hard_ham.tar.bz2": "ham",
    "20030228_spam.tar.bz2": "spam",
    "20030228_easy_ham_2.tar.bz2": "ham",
    "20050311_spam_2.tar.bz2": "spam",
}


def decode_subject(value):
    if not value:
        return ""

    try:
        return str(make_header(decode_header(value)))
    except (ValueError, LookupError):
        return str(value)


def extract_text(message: Message) -> str:
    parts = []

    if message.is_multipart():
        for part in message.walk():
            if part.get_content_maintype() == "multipart":
                continue

            if part.get_content_disposition() == "attachment":
                continue

            if part.get_content_type() == "text/plain":
                try:
                    content = part.get_content()
                    if isinstance(content, str):
                        parts.append(content)
                except (LookupError, UnicodeError):
                    continue
    elif message.get_content_type() == "text/plain":
        try:
            content = message.get_content()
            if isinstance(content, str):
                parts.append(content)
        except (LookupError, UnicodeError):
            pass

    return "\n".join(parts).strip()


def prepare_dataset():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    missing_archives = []

    for filename, label in ARCHIVES.items():
        archive_path = RAW_DIR / filename

        if not archive_path.exists():
            missing_archives.append(filename)
            continue

        print(f"Procesando {filename}...")

        with tarfile.open(archive_path, mode="r:bz2") as archive:
            for member in archive.getmembers():
                if not member.isfile():
                    continue

                # Evitamos leer archivos enormes o vacíos.
                if member.size <= 0 or member.size > 10_000_000:
                    continue

                file_obj = archive.extractfile(member)
                if file_obj is None:
                    continue

                try:
                    message = BytesParser(
                        policy=policy.default
                    ).parsebytes(file_obj.read())

                    subject = decode_subject(
                        str(message.get("Subject", ""))
                    )
                    body = extract_text(message)
                    text = f"{subject}\n{body}".strip()

                    if text:
                        rows.append({
                            "message": text,
                            "label": label,
                            "source_archive": filename,
                        })

                except Exception as error:
                    print(
                        f"Mensaje omitido: {member.name} "
                        f"({type(error).__name__})"
                    )

    if missing_archives:
        print("\nArchivos no encontrados:")
        for filename in missing_archives:
            print(f" - {filename}")

    if not rows:
        raise RuntimeError(
            "No se extrajeron mensajes. Verifica la descarga "
            "y las rutas de los archivos."
        )

    # CSV UTF-8 para conservar caracteres del texto.
    with OUTPUT_FILE.open(
        "w", encoding="utf-8-sig", newline=""
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["message", "label", "source_archive"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nDataset creado: {OUTPUT_FILE}")
    print(f"Mensajes extraídos: {len(rows)}")
    print(f"Distribución de etiquetas:")

    counts = {}
    for row in rows:
        counts[row["label"]] = counts.get(row["label"], 0) + 1

    for label, count in sorted(counts.items()):
        print(f"  {label}: {count}")


if __name__ == "__main__":
    prepare_dataset()
