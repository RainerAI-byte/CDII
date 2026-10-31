
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError
import tarfile

# Carpeta principal del proyecto.
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Guardaremos los archivos originales aquí.
RAW_DIR = PROJECT_DIR / "data" / "raw"

BASE_URL = "https://spamassassin.apache.org/old/publiccorpus/"

ARCHIVES = {
    "20030228_easy_ham.tar.bz2": "ham",
    "20030228_hard_ham.tar.bz2": "ham",
    "20030228_spam.tar.bz2": "spam",
    "20030228_easy_ham_2.tar.bz2": "ham",
    "20050311_spam_2.tar.bz2": "spam",
}


def download_archives():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    for filename in ARCHIVES:
        destination = RAW_DIR / filename

        if destination.exists() and destination.stat().st_size > 0:
            print(f"Ya descargado: {filename}")
            continue

        url = BASE_URL + filename
        print(f"Descargando: {filename}")

        try:
            with urlopen(url, timeout=60) as response:
                content = response.read()

            # Verificamos que sea un archivo tar.bz2 legible.
            import io
            with tarfile.open(fileobj=io.BytesIO(content), mode="r:bz2"):
                pass

            destination.write_bytes(content)
            print(f"Guardado: {destination.name}")

        except (URLError, TimeoutError, OSError, tarfile.TarError) as error:
            print(f"Error con {filename}: {error}")
            print("No se guardó este archivo. Revisa la URL o la conexión.")


if __name__ == "__main__":
    download_archives()
