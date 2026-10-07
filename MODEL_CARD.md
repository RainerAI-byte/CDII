# Model Card — Fashion-MNIST CNN

## 1. Uso previsto

Este modelo fue desarrollado como ejercicio académico de clasificación de imágenes utilizando el dataset Fashion-MNIST.

Su propósito es comparar un modelo baseline denso con una red neuronal convolucional (CNN) bajo las mismas condiciones experimentales.

### Uso previsto
- Clasificación académica de imágenes de prendas de vestir.
- Evaluación reproducible de modelos de aprendizaje automático.
- Comparación de desempeño y costo computacional.

### Fuera de alcance
- No está diseñado para decisiones médicas, financieras o de seguridad.
- No debe utilizarse como sistema productivo sin validación adicional.
- Los resultados no deben generalizarse automáticamente a otros datasets o dominios.

## 2. Dataset y particiones

Dataset: Fashion-MNIST.

Características:
- 60,000 imágenes de entrenamiento.
- 10,000 imágenes de prueba.
- Resolución: 28 × 28 píxeles.
- Escala de grises.
- 10 clases.
- 1,000 imágenes por clase en el conjunto de prueba utilizado para la evaluación.

Las imágenes fueron normalizadas para el entrenamiento de los modelos.

La comparación entre Dense y CNN utilizó la misma partición de evaluación.

## 3. Métricas globales y por clase

### Comparación global

| Modelo | F1 Macro | Parámetros | Entrenamiento (s) | Inferencia (ms/imagen) |
|---|---:|---:|---:|---:|
| Dense | 0.8634 | 50,890 | 10.12 | 0.0503 |
| CNN | 0.7893 | 19,466 | 127.99 | 0.1372 |

El baseline Dense obtuvo un F1 Macro superior al de la CNN en este experimento.

Diferencia de F1 Macro:

Dense - CNN = 0.0741

La CNN no produjo una mejora predictiva respecto al baseline.

### Métricas por clase — CNN

| Clase | Precision | Recall | F1 |
|---:|---:|---:|---:|
| 0 | 0.645 | 0.807 | 0.717 |
| 1 | 0.988 | 0.932 | 0.959 |
| 2 | 0.705 | 0.642 | 0.672 |
| 3 | 0.753 | 0.843 | 0.796 |
| 4 | 0.661 | 0.663 | 0.662 |
| 5 | 0.950 | 0.885 | 0.916 |
| 6 | 0.500 | 0.374 | 0.428 |
| 7 | 0.855 | 0.952 | 0.901 |
| 8 | 0.917 | 0.937 | 0.927 |
| 9 | 0.935 | 0.896 | 0.915 |

La clase con menor F1 fue la clase 6, con 0.428, por lo que constituye la principal dificultad observada en este benchmark.

## 4. Comparación de costo

- Hardware: CPU, ejecución en Windows 11.
- GPU: no disponible en el entorno utilizado.
- Framework: TensorFlow 2.21.0 / Keras 3.15.1.
- Parámetros Dense: 50,890.
- Parámetros CNN: 19,466.
- Tiempo de entrenamiento Dense: 10.12 segundos.
- Tiempo de entrenamiento CNN: 127.99 segundos.
- Inferencia Dense: 0.0503 ms/imagen.
- Inferencia CNN: 0.1372 ms/imagen.
- Tamaño del modelo CNN serializado: aproximadamente 268 KB.

La CNN tiene menos parámetros que el baseline Dense, pero presentó un costo de entrenamiento considerablemente mayor.

El entrenamiento de la CNN tardó aproximadamente 12.6 veces más que el Dense.

La inferencia de la CNN fue aproximadamente 2.7 veces más lenta por imagen.

## 5. Decisión técnica y Green AI

En este experimento, la mejora predictiva de la CNN no justificó su mayor costo computacional.

El modelo Dense obtuvo:
- F1 Macro: 0.8634
- Entrenamiento: 10.12 s
- Inferencia: 0.0503 ms/imagen

La CNN obtuvo:
- F1 Macro: 0.7893
- Entrenamiento: 127.99 s
- Inferencia: 0.1372 ms/imagen

Por tanto, para las condiciones de este benchmark, se seleccionaría el modelo Dense como alternativa más eficiente.

Esta decisión está limitada al dataset, partición, arquitectura, número de épocas, hardware y configuración utilizada.

## 6. Limitaciones y riesgos

- Fashion-MNIST es un benchmark académico y no representa necesariamente imágenes reales de productos.
- El rendimiento depende de la arquitectura y de las ocho épocas utilizadas.
- La CNN puede requerir mayor ajuste de hiperparámetros para competir con el baseline.
- Los resultados obtenidos en CPU no representan necesariamente el costo en GPU u otro hardware.
- Las clases presentan distintos niveles de dificultad; la clase 6 presentó el menor F1.
- La matriz de confusión y los errores visuales deben interpretarse dentro del contexto del benchmark.

## 7. Supervisión y monitoreo

Antes de utilizar el modelo en un contexto real sería necesario:

- Validar el modelo con datos representativos del dominio objetivo.
- Monitorear cambios en la distribución de las imágenes.
- Revisar periódicamente las métricas globales y por clase.
- Analizar errores de clasificación.
- Establecer criterios para reentrenamiento.
- Mantener registro de versiones del modelo y del dataset.

## 8. Reproducibilidad

Artefactos generados:

- eports/cv_metrics.json
- eports/confusion_cnn.png
- eports/cnn_errors.png
- models/best_cnn.keras

Pruebas automatizadas:

2 passed, 1 skipped

El experimento fue ejecutado con Python 3.12.14, TensorFlow 2.21.0 y Keras 3.15.1 sobre Windows 11.

