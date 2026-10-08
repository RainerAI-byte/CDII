# Model Card - Fashion-MNIST CNN

## 1. Identificacion

**Proyecto:** INF-8239 - Unidad 02 - Ejercicio 04
**Tarea:** clasificacion multiclase de imagenes Fashion-MNIST
**Modelos:** red neuronal densa y red neuronal convolucional (CNN)

## 2. Uso previsto

Este modelo fue desarrollado con fines academicos para estudiar un flujo reproducible de clasificacion de imagenes y comparar el desempeño predictivo y costo computacional de una red densa frente a una CNN.

### Fuera de alcance

No esta diseñado para decisiones medicas, financieras, legales, de seguridad u otros contextos de alto impacto. No debe utilizarse en produccion sin una validacion adicional.

## 3. Dataset y particion

Se utilizo Fashion-MNIST:

- 70,000 imagenes en total.
- 60,000 imagenes originales de entrenamiento.
- 10,000 imagenes de prueba.
- 28 x 28 pixeles.
- Escala de grises.
- 10 clases.
- 54,000 imagenes para entrenamiento.
- 6,000 imagenes para validacion.
- 10,000 imagenes para prueba final.
- Semilla principal: 42.

El conjunto de prueba permanecio separado del entrenamiento y la validacion.

## 4. Resultados finales

| Modelo | F1 Macro | Parametros | Entrenamiento (s) | Inferencia (ms/imagen) |
|---|---:|---:|---:|---:|
| Dense | **0.863381** | 50,890 | **7.719** | **0.0480** |
| CNN | 0.789303 | 19,466 | 116.989 | 0.1417 |

La diferencia absoluta de F1 Macro fue de **0.074079 puntos a favor del modelo Dense**.

La CNN requirio aproximadamente **15.15 veces mas tiempo de entrenamiento** y **2.95 veces mas tiempo de inferencia por imagen**.

La CNN utilizo aproximadamente **61.7 % menos parametros**, pero esta reduccion no compenso su menor F1 Macro ni su mayor costo temporal en las condiciones evaluadas.

## 5. Metricas por clase de la CNN

| Clase | Precision | Recall | F1 |
|---:|---:|---:|---:|
| 0 | 0.645 | 0.807 | 0.717 |
| 1 | 0.988 | 0.932 | **0.959** |
| 2 | 0.705 | 0.642 | 0.672 |
| 3 | 0.753 | 0.843 | 0.796 |
| 4 | 0.661 | 0.663 | 0.662 |
| 5 | 0.950 | 0.885 | 0.916 |
| 6 | 0.500 | 0.374 | **0.428** |
| 7 | 0.855 | 0.952 | 0.901 |
| 8 | 0.917 | 0.937 | 0.927 |
| 9 | 0.935 | 0.896 | 0.915 |

La clase 6 presento el menor F1, mientras que la clase 1 presento el mayor. Esto permite identificar las principales diferencias de dificultad entre clases.

## 6. Evidencia visual

Se generaron las siguientes evidencias:

- reports/training_curves.png - curvas de accuracy y loss.
- reports/confusion_cnn.png - matriz de confusion.
- reports/cnn_errors.png - ejemplos de errores de clasificacion.

Estas visualizaciones complementan las metricas numericas y permiten analizar el comportamiento del modelo durante y despues del entrenamiento.

## 7. Costo computacional y Green AI

La comparacion de costo utiliza tiempo de entrenamiento, tiempo de inferencia y numero de parametros como indicadores operacionales.

- Hardware: CPU sobre Windows 11.
- TensorFlow: 2.21.0.
- Keras: 3.15.1.
- Dense: 50,890 parametros.
- CNN: 19,466 parametros.
- Entrenamiento Dense: 7.719 segundos.
- Entrenamiento CNN: 116.989 segundos.
- Inferencia Dense: 0.0480 ms/imagen.
- Inferencia CNN: 0.1417 ms/imagen.
- Tamaño serializado de CNN: aproximadamente 268 KB.

No se realizo una medicion directa de consumo electrico ni emisiones de CO2. Por tanto, los resultados representan una comparacion relativa del costo computacional bajo las condiciones de ejecucion utilizadas.

## 8. Decision tecnica

El modelo Dense es la alternativa seleccionada para este benchmark.

La decision se fundamenta en que obtuvo mayor F1 Macro y menor costo temporal de entrenamiento e inferencia. Aunque la CNN utiliza menos parametros, no alcanzo el desempeño del baseline.

Esta conclusion esta limitada al dataset, particion, arquitectura, ocho epocas, hardware y configuracion utilizados.

## 9. Limitaciones

- Fashion-MNIST es un benchmark academico y no representa necesariamente imagenes reales de productos.
- El rendimiento depende de la arquitectura y de las ocho epocas utilizadas.
- La CNN podria requerir ajuste adicional de hiperparametros para competir con el baseline.
- Los resultados en CPU no representan necesariamente el costo en GPU.
- Las clases presentan distintos niveles de dificultad.
- El analisis de costo no equivale a una medicion directa de energia o emisiones.

## 10. Reproducibilidad

Artefactos principales:

- 
otebooks/01_e04_evidencias_cv.ipynb
- scripts/train_cv.py
- scripts/check_runtime.py
- reports/cv_metrics.json
- reports/training_curves.png
- reports/confusion_cnn.png
- reports/cnn_errors.png
- models/best_cnn.keras
- equirements.txt`n
Pruebas automatizadas:

**2 passed, 1 skipped**

Entorno verificado:

- Python 3.12.14
- TensorFlow 2.21.0
- Keras 3.15.1
- Windows 11
- CPU

## 11. Uso responsable de IA

Se utilizo asistencia de herramientas de inteligencia artificial para:

- interpretar errores y advertencias tecnicas;
- proponer y revisar pruebas;
- apoyar la organizacion de la documentacion;
- revisar aspectos de redaccion tecnica.

Las ejecuciones del codigo, metricas, archivos generados y conclusiones fueron verificadas localmente en el entorno del proyecto.

Las correcciones realizadas incluyeron la revision de advertencias de TensorFlow, validacion de pruebas, actualizacion de evidencias visuales y correccion de la documentacion para reflejar los resultados de la ejecucion final.

La responsabilidad sobre los datos, codigo, resultados, referencias y conclusiones corresponde al estudiante.





