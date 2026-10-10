# Declaración de uso de inteligencia artificial

## 1. Herramientas utilizadas

- Python y TensorFlow/Keras para implementar y entrenar los modelos.
- NumPy para las operaciones numéricas y la generación de puntos latentes.
- Matplotlib para producir las visualizaciones.
- Streamlit para construir una interfaz de exploración del espacio latente.
- ChatGPT como herramienta de asistencia durante la revisión técnica, la interpretación de resultados y la preparación de documentación.

## 2. Propósito de cada uso

TensorFlow/Keras se utilizó para construir, entrenar y guardar los modelos Autoencoder y VAE.

NumPy se utilizó para normalizar y manipular datos, establecer semillas y construir puntos latentes para generación e interpolación.

Matplotlib se utilizó para comparar imágenes originales, reconstrucciones y muestras generadas.

Streamlit se utilizó para permitir la exploración interactiva del decodificador mediante dos coordenadas latentes.

ChatGPT se utilizó como apoyo para analizar el código, explicar conceptos, organizar la documentación y revisar las limitaciones metodológicas. La asistencia de una herramienta generativa no sustituye la validación del código ni la responsabilidad del estudiante sobre el trabajo entregado.

## 3. Prompts o decisiones relevantes

Las solicitudes de asistencia se centraron en:

- Explicar la diferencia entre un Autoencoder y un Variational Autoencoder.
- Revisar el flujo de entrenamiento y la interpretación de las pérdidas.
- Documentar las arquitecturas y el espacio latente.
- Distinguir las métricas realmente calculadas de las evaluaciones que todavía faltan.
- Identificar riesgos de privacidad, memorización y uso indebido de datos sintéticos.
- Preparar instrucciones reproducibles para ejecutar y validar el proyecto.

Las decisiones técnicas documentadas se contrastaron con los archivos del proyecto y los resultados de la ejecución.

## 4. Elementos verificados por el equipo

Durante la ejecución se verificaron:

- El entorno Python 3.12.14 y TensorFlow 2.21.0.
- La disponibilidad del dataset Fashion-MNIST mediante TensorFlow/Keras.
- La finalización del entrenamiento del Autoencoder y del VAE.
- La generación de los archivos `autoencoder.keras` y `decoder.keras`.
- La creación de las visualizaciones `ae_vae_panel.png` e `interpolation.png`.
- La escritura del archivo `training_metrics.json`.
- La ejecución de las pruebas automatizadas del proyecto.

Las métricas incluidas en la documentación proceden del archivo generado por el script. No se afirma haber realizado evaluaciones de privacidad, detección de memorización, FID, SSIM o PSNR, porque no forman parte de los resultados registrados.

La inspección visual final de las imágenes y la validación funcional de la aplicación deben completarse antes de considerar terminado el control de calidad.

## 5. Cambios realizados sobre resultados generados

La asistencia generativa se utilizó como apoyo para analizar y documentar el proyecto. Las descripciones técnicas se ajustaron al código fuente y a las métricas disponibles, evitando presentar como hechos resultados que no fueron medidos.

La documentación mantiene explícitas las limitaciones del experimento y separa las observaciones verificadas de las comprobaciones pendientes.

Cualquier modificación adicional sugerida por una herramienta de IA debe revisarse, probarse y aceptarse conscientemente antes de incorporarse al proyecto.

## 6. Responsabilidad asumida

El estudiante es responsable de comprender el código entregado, comprobar su ejecución, revisar los resultados y cumplir las normas académicas aplicables a la asignatura.

La generación de imágenes sintéticas no garantiza privacidad, anonimato, originalidad ni ausencia de memorización. No se realizan esas afirmaciones sin pruebas específicas.

Las conclusiones se limitan a la ejecución, al dataset, a las arquitecturas y a las métricas descritas en la documentación.
