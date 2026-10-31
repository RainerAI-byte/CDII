# SpamShield — Detección de correo no deseado mediante NLP

## 1. Descripción

SpamShield es un proyecto académico de procesamiento del lenguaje natural (NLP) que compara modelos de aprendizaje automático para clasificar correos electrónicos como legítimos (`ham`) o no deseados (`spam`).

El proyecto utiliza el SpamAssassin Public Corpus y evalúa un modelo de referencia (*baseline*), Naive Bayes y Regresión Logística.

## 2. Objetivos

- Preparar y auditar los datos.
- Evitar duplicados y registros inválidos.
- Entrenar y comparar modelos con una partición reproducible.
- Evaluar precisión, recall, F1 Macro y matrices de confusión.
- Documentar las decisiones, limitaciones y resultados.

## 3. Dataset

El archivo procesado se encuentra en `data/processed/emails_clean.csv`.

- Registros después de la limpieza: 5,897.
- Correos legítimos (`ham`): 4,111.
- Correos spam: 1,786.
- Partición: 80 % entrenamiento y 20 % prueba.
- Semilla aleatoria: 42.
- División estratificada por clase.

La columna `message` contiene el texto y `label` identifica la clase. `source_archive` se conserva para trazabilidad y no debe utilizarse como predictor.

## 4. Resultados experimentales

| Modelo | Accuracy | F1 Macro | Precisión spam | Recall spam |
|---|---:|---:|---:|---:|
| Baseline | 0.6975 | 0.4109 | 0.0000 | 0.0000 |
| Naive Bayes | 0.9246 | 0.9035 | 0.9926 | 0.7563 |
| Regresión Logística | 0.9695 | 0.9634 | 0.9707 | 0.9272 |

La Regresión Logística obtuvo el mayor F1 Macro y detectó 331 de los 357 mensajes spam del conjunto de prueba. Naive Bayes generó menos falsos positivos: 2, frente a 10 de la Regresión Logística.

La selección final depende del costo relativo de los falsos positivos y falsos negativos. Estos resultados corresponden a la partición experimental utilizada y no garantizan el mismo rendimiento con correos nuevos.

## 5. Estructura del proyecto

- `data/raw/`: archivos originales.
- `data/interim/`: datos intermedios.
- `data/processed/`: datos preparados y limpios.
- `src/`: scripts de preparación, auditoría, entrenamiento y reportes.
- `tests/`: pruebas automatizadas.
- `models/`: modelos serializados.
- `reports/results/`: métricas y archivos CSV/JSON.
- `reports/figures/`: visualizaciones.
- `docs/`: ficha del dataset, decisiones y model card.
- `demo/`: espacio para la demostración del clasificador.

## 6. Requisitos

Se recomienda utilizar el entorno virtual del proyecto e instalar las dependencias declaradas en `requirements.txt`.

```powershell
python -m pip install -r requirements.txt
```

## 7. Ejecución

Desde la raíz del repositorio y con el entorno virtual activado:

```powershell
python src/clean_data.py
python src/audit_data.py
python src/train_models.py
python src/generate_reports.py
python -m pytest -v
```

Los scripts deben ejecutarse en orden. El entrenamiento vuelve a generar los modelos y las métricas; no es necesario repetirlo si solo se desea consultar los resultados existentes.

## 8. Artefactos principales

- `models/logistic_regression.joblib`
- `models/naive_bayes.joblib`
- `models/baseline.joblib`
- `reports/results/model_comparison.csv`
- `reports/results/confusion_matrices.csv`
- `reports/results/recomputed_metrics.csv`
- `reports/figures/confusion_matrices.png`

## 9. Limitaciones

El corpus contiene mensajes históricos y puede no representar el spam actual. Los encabezados, las firmas y los mensajes relacionados pueden introducir señales que no se generalicen a otros conjuntos de datos. La evaluación utiliza una partición aleatoria y no sustituye una validación temporal o externa.

El sistema es una herramienta experimental de clasificación; sus predicciones no deben interpretarse como infalibles.

## 10. Documentación complementaria

- `docs/ficha_dataset.md`
- `docs/decisiones.md`
- `docs/model_card.md`

## 11. Demostración interactiva

Para ejecutar el clasificador utilizando el modelo de Regresión Logística ya serializado:

```powershell
python demo/predict_email.py
```

Introduce un mensaje cuando el programa lo solicite. Para terminar, escribe `salir`.

La demostración muestra la clasificación y, cuando está disponible, una probabilidad estimada de spam. Esta probabilidad no es una garantía ni implica que el modelo esté perfectamente calibrado.

## 12. Pruebas automatizadas

Ejecuta las pruebas desde la raíz del proyecto:

```powershell
python -m pytest -v
```

En la última ejecución registrada se aprobaron 12 pruebas automatizadas.
