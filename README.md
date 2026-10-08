# INF-8239 - Unidad 02 - Proyecto E04 - Vision Computacional

## Descripcion

Proyecto academico de clasificacion de imagenes con Fashion-MNIST. Se comparan un baseline de red neuronal densa y una red neuronal convolucional (CNN), utilizando la misma particion y condiciones experimentales.

## Entorno

- Python 3.12.14
- TensorFlow 2.21.0
- Keras 3.15.1
- Windows 11
- Ejecucion final sobre CPU

## Ejecucion

``bash
uv python install 3.12
uv sync --extra cpu
uv run python scripts/check_runtime.py
uv run python scripts/train_cv.py --epochs 8
uv run jupyter nbconvert --to notebook --execute notebooks/01_e04_evidencias_cv.ipynb --inplace
``

## Resultados finales

| Modelo | F1 Macro | Parametros | Entrenamiento (s) | Inferencia (ms/imagen) |
|---|---:|---:|---:|---:|
| Dense | **0.863381** | 50,890 | **7.719** | **0.0480** |
| CNN | 0.789303 | 19,466 | 116.989 | 0.1417 |

La red densa obtuvo el mejor F1 Macro. La diferencia fue de **0.074079 puntos**. La CNN requirio aproximadamente **15.15 veces mas tiempo de entrenamiento** y **2.95 veces mas tiempo de inferencia por imagen**. Aunque utilizo aproximadamente **61.7 % menos parametros**, no supero al baseline.

La decision final favorece el **modelo denso** bajo las condiciones de este experimento.

## Evidencias

- `reports/cv_metrics.json` - metricas finales.
- `reports/training_curves.png` - curvas de aprendizaje.
- `reports/confusion_cnn.png` - matriz de confusion.
- `reports/cnn_errors.png` - errores de clasificacion.
- `models/best_cnn.keras` - modelo CNN serializado.
- `notebooks/01_e04_evidencias_cv.ipynb` - notebook ejecutado.

## Pruebas

**2 passed, 1 skipped**

## Documentacion

- `MODEL_CARD.md` - ficha tecnica del modelo.
- `requirements.txt` - dependencias principales.
- `requirements-colab.txt` - dependencias para Colab.

## Uso de IA

Se utilizo asistencia de herramientas de inteligencia artificial para interpretar errores tecnicos, proponer y revisar pruebas y apoyar la organizacion de la documentacion. Las ejecuciones, metricas, artefactos y conclusiones fueron verificadas localmente. La responsabilidad final corresponde al estudiante.

