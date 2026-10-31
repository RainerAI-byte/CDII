# Decisiones experimentales — SpamShield

## 1. Objetivo

Comparar un baseline y dos clasificadores supervisados para detectar correo no deseado, evaluando desempeño predictivo y costo computacional.

## 2. Definición del problema

Se trata de una clasificación binaria de texto:

- `ham`: correo legítimo.
- `spam`: correo no deseado.

La variable de entrada es `message`; la variable objetivo es `label`. El campo `source_archive` se excluye de las entradas predictoras.

## 3. Preparación de los datos

Se eliminaron mensajes nulos, vacíos y repetidos por texto. El conjunto final contiene 5,897 mensajes: 4,111 ham y 1,786 spam.

La partición se realizó con 80 % para entrenamiento y 20 % para prueba, usando estratificación y `random_state=42`. La partición no debe modificarse al comparar los modelos.

## 4. Modelos

### Baseline

`DummyClassifier(strategy="most_frequent")`

Sirve como referencia mínima. Predice siempre la clase mayoritaria, ham. No es una solución útil para detectar spam, pero permite comprobar si los modelos supervisados mejoran sobre una estrategia trivial.

### Naive Bayes

Pipeline con TF-IDF y `MultinomialNB(alpha=0.5)`. Es un modelo probabilístico clásico para clasificación de texto.

### Regresión Logística

Pipeline con TF-IDF y `LogisticRegression(max_iter=1000, random_state=42)`. Se incluye como clasificador lineal capaz de aprender pesos para los términos y combinaciones de términos.

En ambos modelos de texto se utilizan minúsculas, normalización de acentos, unigramas y bigramas, y un máximo de 50,000 características.

## 5. Métricas

- Accuracy: proporción total de predicciones correctas.
- F1 Macro: media del F1 de las clases, dando el mismo peso a ham y spam.
- Precision de spam: proporción de mensajes predichos como spam que realmente son spam.
- Recall de spam: proporción de los mensajes spam reales que se detectan.
- Average Precision (AP): resumen de la precisión a distintos niveles de recall, calculado a partir de las puntuaciones del modelo.
- Tiempo de entrenamiento e inferencia: medidas operacionales del costo computacional.

Se presta especial atención al recall de spam porque los falsos negativos son correos no deseados que no se detectan. También se revisan los falsos positivos, porque un correo legítimo podría clasificarse erróneamente como spam.

## 6. Resultados observados

| Modelo | Accuracy | F1 Macro | Precision spam | Recall spam | TN | FP | FN | TP |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Baseline | 0.697458 | 0.410884 | 0.000000 | 0.000000 | 823 | 0 | 357 | 0 |
| Naive Bayes | 0.924576 | 0.903545 | 0.992647 | 0.756303 | 821 | 2 | 87 | 270 |
| Regresión Logística | 0.969492 | 0.963382 | 0.970674 | 0.927171 | 813 | 10 | 26 | 331 |

## 7. Interpretación y selección provisional

Regresión Logística obtiene el mejor F1 Macro y el mayor recall de spam. Detecta 331 de los 357 mensajes spam del conjunto de prueba y deja pasar 26.

Naive Bayes tiene mayor precision de spam y produce solo dos falsos positivos, pero deja pasar 87 mensajes spam.

Por tanto, Regresión Logística es el candidato principal cuando se prioriza detectar una proporción mayor del spam. Naive Bayes puede resultar preferible en escenarios donde el costo de marcar un correo legítimo como spam sea especialmente alto.

La selección definitiva debe considerar los costos del contexto de uso y las limitaciones del corpus. Las métricas no justifican eliminar o bloquear correos automáticamente sin mecanismos de revisión y recuperación.

## 8. Interpretación del baseline y de AP

El baseline predice todos los mensajes como ham. Por ello, su recall de spam y su precision de spam son cero.

El CSV registra un Average Precision aproximado de 0.302542 para el baseline, igual a la prevalencia de spam en el conjunto de prueba. Como sus puntuaciones no discriminan entre mensajes, ese valor no representa una capacidad útil de ordenar los mensajes por probabilidad de spam. Debe interpretarse como una referencia degenerada y no como evidencia de que el baseline detecta spam.

## 9. Reproducibilidad y limitaciones

La partición, las métricas y los modelos se registran en `reports/results/`. Las matrices de confusión se guardan en `reports/results/confusion_matrices.csv` y la figura comparativa en `reports/figures/confusion_matrices.png`.

La medición del tiempo depende del hardware, el entorno y la carga del equipo. No se midieron directamente consumo eléctrico ni emisiones de CO₂. Por tanto, el tiempo de ejecución es un indicador operacional, no una medición directa de energía.

La partición aleatoria puede no reflejar la generalización temporal a campañas nuevas. Los resultados deben entenderse dentro de las condiciones de este experimento.

