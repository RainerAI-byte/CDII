# Conclusión — U01.LAB02

En este laboratorio se realizó la búsqueda, selección y auditoría de un dataset público para adaptar el flujo de clasificación desarrollado en LAB01 a un problema de datos reales. Se seleccionaron dos candidatos provenientes del UCI Machine Learning Repository y se evaluaron considerando procedencia, licencia, cantidad de registros, variable objetivo, número de clases, valores ausentes, compatibilidad con CPU y posibles riesgos de fuga de información.

El dataset seleccionado fue **Predict Students' Dropout and Academic Success**, compuesto por 4,424 registros y 36 variables predictoras. Cada registro representa un estudiante universitario y la variable objetivo `Target` contiene tres categorías: `Dropout`, `Enrolled` y `Graduate`. La documentación oficial de UCI identifica el problema como una tarea de clasificación multiclase y señala que no existen valores faltantes.

La descarga fue implementada de manera reproducible mediante una función en `src/inf8239_u01/data.py`, evitando depender de una ruta personal del equipo. Posteriormente se realizó una auditoría del esquema, se verificó la variable objetivo y se construyó un pipeline de preprocesamiento. La división de los datos utilizó 80 % para entrenamiento y 20 % para prueba, con `random_state=42` y estratificación.

Como línea base se utilizó `DummyClassifier`, obteniendo un F1 macro de 0.2221. El modelo SVM con kernel RBF obtuvo un F1 macro de 0.6785, mientras que su accuracy fue de 0.76. El desempeño por clase mostró diferencias, particularmente en `Enrolled`, cuyo F1 fue de 0.41, frente a 0.78 para `Dropout` y 0.84 para `Graduate`.

Un aspecto relevante de la auditoría fue identificar que el dataset contiene variables académicas correspondientes al primer y segundo semestre. Estas variables pueden presentar un riesgo de disponibilidad temporal si el objetivo de predicción se establece exclusivamente al momento de la matrícula. Por ello, este riesgo fue documentado y no se eliminaron variables únicamente por su efecto sobre las métricas.

Finalmente, se implementó un contrato de datos con pruebas automatizadas. La ejecución de `pytest` produjo **4 pruebas aprobadas**, lo que aporta una verificación reproducible de la estructura mínima esperada del dataset.
