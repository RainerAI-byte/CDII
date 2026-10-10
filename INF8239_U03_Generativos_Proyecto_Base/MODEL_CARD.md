# Model Card - Autoencoder y VAE

## 1. Modelos y versiones

Proyecto académico de INF-8239 Ciencia de Datos II, Unidad 03.

Se implementaron dos modelos generativos basados en redes neuronales:

- **Autoencoder (AE):** comprime cada imagen en un vector latente de 16 dimensiones y reconstruye la imagen a partir de esa representación.
- **Variational Autoencoder (VAE):** aprende una distribución latente de 2 dimensiones y utiliza un decodificador para reconstruir o generar imágenes.

Framework: TensorFlow/Keras 2.21.0.
Lenguaje: Python 3.12.
Semilla configurada: 42.
Ejecución documentada: CPU en Windows 11.

## 2. Uso previsto y usuarios

El propósito es educativo y experimental. Los modelos permiten estudiar:

- Compresión y reconstrucción de imágenes.
- Representaciones latentes.
- Generación de muestras mediante un VAE.
- Interpolación entre puntos del espacio latente.
- Diferencias entre un Autoencoder convencional y un VAE.

Los usuarios previstos son estudiantes, docentes y personas que investigan los fundamentos de los modelos generativos.

## 3. Usos fuera de alcance

Los modelos no están diseñados ni validados para:

- Diagnóstico médico o decisiones de alto impacto.
- Identificación de personas.
- Generación de imágenes comerciales de calidad profesional.
- Garantizar originalidad, privacidad o ausencia de memorización.
- Detectar automáticamente contenido falso.
- Representar de manera fiable todas las categorías de prendas en contextos reales.

No deben utilizarse para tomar decisiones importantes sin evaluación adicional.

## 4. Dataset, licencia y particiones

Se utiliza Fashion-MNIST mediante `tf.keras.datasets.fashion_mnist.load_data()`.

El conjunto estándar contiene 60,000 imágenes de entrenamiento y 10,000 imágenes de prueba. Las imágenes son en escala de grises, de 28 x 28 píxeles, y representan categorías de artículos de vestir.

En este experimento se descartan las etiquetas de clase porque el objetivo es reconstruir y generar imágenes, no clasificarlas.

Las imágenes se convierten a `float32`, se normalizan al intervalo [0, 1] y se añade un canal para obtener la forma (28, 28, 1).

El Autoencoder utiliza `validation_split=0.1` sobre los datos de entrenamiento. El VAE se entrena con los datos de entrenamiento y no utiliza una partición de validación explícita en el código actual.

Las imágenes de prueba se emplean para construir una visualización de 12 ejemplos. El script no calcula una métrica agregada de reconstrucción sobre todo el conjunto de prueba.

La fuente de carga es TensorFlow/Keras. La licencia y las condiciones de redistribución del dataset original deben comprobarse en la fuente oficial antes de redistribuir los datos.

## 5. Arquitectura y espacio latente

### Autoencoder

- Entrada: 28 x 28 x 1.
- Aplanamiento de la imagen a 784 valores.
- Capa latente densa de 16 unidades con activación ReLU.
- Capa densa de 784 unidades con activación sigmoide.
- Reconstrucción a la forma 28 x 28 x 1.
- Optimizador: Adam.
- Función de pérdida: entropía cruzada binaria.
- Tamaño registrado: 25,888 parámetros.

### Variational Autoencoder

El codificador contiene:

- Entrada de 28 x 28 x 1.
- Aplanamiento a 784 valores.
- Capa densa de 128 unidades con activación ReLU.
- Dos salidas latentes: media y log-varianza, cada una de 2 dimensiones.

El decodificador contiene:

- Entrada latente de 2 dimensiones.
- Capa densa de 128 unidades con activación ReLU.
- Capa densa de 784 unidades con activación sigmoide.
- Reconstrucción de 28 x 28 x 1.

La pérdida combina el error de reconstrucción y la divergencia KL. Durante el entrenamiento se muestrea el vector latente mediante la media, la log-varianza y ruido aleatorio.

El archivo `decoder.keras` almacena el decodificador del VAE. No equivale al modelo VAE completo ni contiene por sí solo el codificador.

## 6. Métricas de reconstrucción y generación

La ejecución documentada registró los siguientes resultados:

| Indicador | Resultado |
|---|---:|
| Épocas máximas del Autoencoder | 6 |
| Épocas del VAE | 8 |
| Tiempo de entrenamiento del Autoencoder | 12.20 s |
| Tiempo de entrenamiento del VAE | 16.76 s |
| Parámetros del Autoencoder | 25,888 |
| Parámetros del decodificador VAE | 101,520 |

Los tiempos corresponden a una ejecución específica y dependen del hardware, del software y de las condiciones del sistema.

El archivo `reports/training_metrics.json` no registra métricas cuantitativas de calidad generativa. Por tanto, no se presentan valores de SSIM, PSNR, FID, diversidad, precisión perceptual ni error de reconstrucción sobre todo el conjunto de prueba.

La calidad de las imágenes generadas debe interpretarse como una evaluación visual exploratoria, no como una validación cuantitativa completa.

## 7. Diversidad y vecinos cercanos

El script genera 12 muestras utilizando vectores aleatorios de una distribución normal estándar en el espacio latente de 2 dimensiones.

También genera una secuencia de 12 puntos interpolados entre (-2, -1) y (2, 1).

Estas visualizaciones permiten explorar el comportamiento del decodificador. No demuestran por sí solas diversidad suficiente, ausencia de memorización ni independencia respecto de las imágenes de entrenamiento.

No se implementó una búsqueda de vecinos cercanos ni una evaluación formal de duplicados en el código documentado.

## 8. Hardware, tiempo y tamaño

La ejecución registrada se realizó en Windows 11 con Python 3.12.14 y TensorFlow 2.21.0, utilizando CPU.

TensorFlow informó que no disponía de soporte GPU para esta instalación nativa de Windows. El entrenamiento terminó correctamente en CPU.

Los tiempos registrados fueron:

- Autoencoder: 12.20 segundos.
- VAE: 16.76 segundos.

Los archivos de modelo generados son:

- `models/autoencoder.keras`
- `models/decoder.keras`

Los tiempos no deben extrapolarse a otros equipos sin realizar mediciones comparables.

## 9. Limitaciones, riesgos y supervisión

Las imágenes de Fashion-MNIST son pequeñas, monocromáticas y pertenecen a un dominio acotado. El comportamiento observado no garantiza resultados equivalentes con fotografías reales o conjuntos de datos diferentes.

El espacio latente reducido del VAE facilita la visualización, pero también limita la capacidad de representación.

La evaluación actual se centra en las pérdidas de entrenamiento mostradas durante el ajuste, los tiempos, el número de parámetros y las visualizaciones generadas. Faltan métricas cuantitativas independientes para valorar de forma más completa la reconstrucción, la diversidad y la calidad de las muestras.

Los datos sintéticos no son automáticamente anónimos ni privados. Un modelo puede reproducir patrones o memorizar características del conjunto de entrenamiento. Se requieren evaluaciones específicas antes de realizar afirmaciones de privacidad.

La revisión humana es necesaria para interpretar las visualizaciones y determinar si el modelo resulta adecuado para un uso concreto.

## 10. Artefactos

- `scripts/train_ae_vae.py`: entrenamiento y generación de visualizaciones.
- `src/inf8239_u03_gen/models.py`: arquitecturas del Autoencoder, codificador y decodificador.
- `src/inf8239_u03_gen/data.py`: normalización y validación de imágenes.
- `reports/training_metrics.json`: tiempos y parámetros registrados.
- `reports/ae_vae_panel.png`: originales, reconstrucciones y muestras generadas.
- `reports/interpolation.png`: secuencia de interpolación latente.
- `models/autoencoder.keras`: Autoencoder entrenado.
- `models/decoder.keras`: decodificador del VAE entrenado.
