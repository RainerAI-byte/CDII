from __future__ import annotations

import json
from pathlib import Path
from time import perf_counter

import numpy as np
import tensorflow as tf

from inf8239_u03_gen.data import normalize_images

ROOT = Path(__file__).resolve().parents[1]
SEED = 42
N_EVAL = 1000
N_GENERATED = 500


def reconstruction_metrics(originals, reconstructed):
    originals = np.asarray(originals, dtype=np.float32)
    reconstructed = np.asarray(reconstructed, dtype=np.float32)

    return {
        "mse": float(np.mean((originals - reconstructed) ** 2)),
        "mae": float(np.mean(np.abs(originals - reconstructed))),
    }


def diversity_metrics(images):
    """Diversidad exploratoria mediante MAE entre pares de imágenes."""
    images = np.asarray(images, dtype=np.float32).reshape(len(images), -1)

    if len(images) < 2:
        return {"mean_pairwise_mae": None}

    distances = []
    for i in range(len(images) - 1):
        distances.extend(np.mean(np.abs(images[i + 1:] - images[i]), axis=1))

    return {"mean_pairwise_mae": float(np.mean(distances))}


def nearest_training_mae(generated, training_images):
    """Distancia MAE al vecino de entrenamiento más parecido."""
    generated = np.asarray(generated, dtype=np.float32).reshape(len(generated), -1)
    training_images = np.asarray(training_images, dtype=np.float32).reshape(
        len(training_images), -1
    )

    result = []
    for image in generated:
        distances = np.mean(np.abs(training_images - image), axis=1)
        result.append(float(np.min(distances)))

    return {
        "mean_nearest_train_mae": float(np.mean(result)),
        "min_nearest_train_mae": float(np.min(result)),
    }


def main():
    rng = np.random.default_rng(SEED)

    (x_train, _), (x_test, _) = tf.keras.datasets.fashion_mnist.load_data()
    x_train = normalize_images(x_train)
    x_test = normalize_images(x_test)

    # Subconjuntos deterministas para reducir el costo de evaluación.
    train_idx = rng.choice(len(x_train), size=min(5000, len(x_train)), replace=False)
    test_idx = rng.choice(len(x_test), size=min(N_EVAL, len(x_test)), replace=False)

    train_reference = x_train[train_idx]
    test_images = x_test[test_idx]

    ae = tf.keras.models.load_model(ROOT / "models" / "autoencoder.keras")
    decoder = tf.keras.models.load_model(ROOT / "models" / "decoder.keras")

    # Evaluación de reconstrucción del AE.
    start = perf_counter()
    ae_reconstruction = ae.predict(test_images, verbose=0)
    ae_inference_seconds = perf_counter() - start

    # El código original no guarda el encoder VAE.
    # Para calcular el error de reconstrucción VAE se debe guardar el encoder
    # durante el entrenamiento y cargarlo aquí.
    encoder_path = ROOT / "models" / "encoder.keras"
    if not encoder_path.exists():
        raise FileNotFoundError(
            "Falta models/encoder.keras. Guarda el encoder VAE al entrenar "
            "y vuelve a ejecutar el script."
        )

    encoder = tf.keras.models.load_model(encoder_path)
    mean, log_variance = encoder.predict(test_images, verbose=0)

    start = perf_counter()
    vae_reconstruction = decoder.predict(mean, verbose=0)
    vae_inference_seconds = perf_counter() - start

    # Generación reproducible desde una distribución normal estándar.
    latent_samples = rng.normal(size=(N_GENERATED, 2)).astype(np.float32)
    generated = decoder.predict(latent_samples, verbose=0)

    results = {
        "seed": SEED,
        "test_examples": len(test_images),
        "training_reference_examples": len(train_reference),
        "generated_examples": len(generated),
        "ae_reconstruction": reconstruction_metrics(
            test_images, ae_reconstruction
        ),
        "vae_reconstruction": reconstruction_metrics(
            test_images, vae_reconstruction
        ),
        "ae_inference_seconds_total": float(ae_inference_seconds),
        "vae_inference_seconds_total": float(vae_inference_seconds),
        "ae_inference_ms_per_image": float(
            1000 * ae_inference_seconds / len(test_images)
        ),
        "vae_inference_ms_per_image": float(
            1000 * vae_inference_seconds / len(test_images)
        ),
        "vae_generated_diversity": diversity_metrics(generated),
        "vae_generated_nearest_training": nearest_training_mae(
            generated, train_reference
        ),
    }

    output = ROOT / "reports" / "evaluation_metrics.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()