from pathlib import Path

import joblib


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "logistic_regression.joblib"


def load_model():
    """Carga el modelo entrenado desde disco."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"No se encontró el modelo: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


def predict_email(model, message):
    """Clasifica un correo y devuelve su probabilidad estimada de spam."""
    message = message.strip()

    if not message:
        raise ValueError("El mensaje no puede estar vacío.")

    prediction = model.predict([message])[0]

    spam_probability = None

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba([message])[0]
        classes = list(model.classes_)

        if "spam" in classes:
            spam_probability = float(
                probabilities[classes.index("spam")]
            )

    return prediction, spam_probability


def main():
    print("=" * 50)
    print("             SPAMSHIELD")
    print(" Detector de correo no deseado")
    print("=" * 50)

    try:
        model = load_model()
    except Exception as error:
        print(f"No fue posible cargar el modelo: {error}")
        return

    while True:
        print("\nEscribe el texto del correo.")
        print("Escribe SALIR para terminar.")

        message = input("\nCorreo: ").strip()

        if message.lower() == "salir":
            print("Demostración finalizada.")
            break

        try:
            prediction, probability = predict_email(model, message)
        except ValueError as error:
            print(f"Entrada no válida: {error}")
            continue

        print("\n--- RESULTADO ---")

        if prediction == "spam":
            print("Clasificación: SPAM")
        else:
            print("Clasificación: CORREO LEGÍTIMO (HAM)")

        if probability is not None:
            print(f"Probabilidad estimada de spam: {probability:.2%}")

        print(
            "Nota: la predicción es una estimación del modelo, "
            "no una garantía."
        )


if __name__ == "__main__":
    main()
