# INF8239_U01 — Ciencia de Datos II

## Unidad 01

Proyecto correspondiente a la Unidad 01 de la asignatura **INF-8239 Ciencia de Datos II**.

El proyecto desarrolla un flujo reproducible de clasificación utilizando el dataset público **Predict Students' Dropout and Academic Success**, disponible en el UCI Machine Learning Repository.

## Dataset

* **Fuente:** UCI Machine Learning Repository
* **Dataset:** Predict Students' Dropout and Academic Success
* **Instancias:** 4,424
* **Variables predictoras:** 36
* **Variable objetivo:** `Target`
* **Clases:** `Dropout`, `Enrolled`, `Graduate`
* **Valores ausentes:** No
* **Licencia:** CC BY 4.0
* **DOI:** 10.24432/C5MC89

La documentación oficial indica que cada instancia representa un estudiante y que el problema corresponde a una clasificación de tres categorías.

## Descarga reproducible

La descarga se realiza mediante:

```text
src/inf8239_u01/data.py
```

La fuente utilizada es la URL oficial del archivo `data.csv` del repositorio UCI.

El dataset descargado se almacena en:

```text
data/raw/dataset.csv
```

## Variable objetivo

La variable `Target` representa el resultado académico final:

* `Dropout`
* `Enrolled`
* `Graduate`

La distribución observada fue:

| Clase    | Registros |
| -------- | --------: |
| Graduate |     2,209 |
| Dropout  |     1,421 |
| Enrolled |       794 |

## Modelo y métrica

Se utiliza un clasificador **SVM con kernel RBF**, siguiendo la estructura desarrollada previamente en LAB01.

La métrica principal es **F1 macro**, debido a que el problema presenta tres clases y existe diferencia en la cantidad de observaciones entre ellas.

Se utiliza un modelo `DummyClassifier` como línea base.

Resultados obtenidos:

| Modelo | F1 macro |
| ------ | -------: |
| Dummy  |   0.2221 |
| SVM    |   0.6785 |

## Preprocesamiento

El preprocesamiento se integra dentro de un `Pipeline`.

Las variables numéricas utilizan:

* imputación por mediana;
* estandarización mediante `StandardScaler`.

Las variables categóricas detectadas automáticamente por su tipo de datos fueron cero, debido a que las variables predictoras del archivo se encuentran codificadas numéricamente.

## Estructura

```text
INF8239_U01/
├── data/
│   └── raw/
│       └── dataset.csv
├── docs/
│   ├── ficha_dataset.md
│   ├── comparacion_datasets.md
│   └── diccionario_variables.md
├── notebooks/
│   ├── 01_svm_guiada.ipynb
│   └── 02_dataset_auditoria.ipynb
├── reports/
├── src/
│   └── inf8239_u01/
│       ├── data.py
│       └── models.py
├── tests/
│   ├── test_data_contract.py
│   └── test_models.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Pruebas

El contrato de datos incluye pruebas para:

1. verificar que el dataset no esté vacío;
2. verificar la existencia de columnas requeridas;
3. verificar que el target no tenga valores faltantes y contenga al menos dos clases.

Resultado de ejecución:

```text
4 passed, 1 warning
```

## Documentación

La ficha del dataset, comparación de candidatos, auditoría y diccionario de variables se encuentran en la carpeta `docs/`.

El notebook de trabajo de LAB02 se encuentra en:

```text
notebooks/02_dataset_auditoria.ipynb
```

## Consideración sobre disponibilidad temporal

El dataset combina información disponible al momento de la matrícula con información académica correspondiente al primer y segundo semestre. Por ello, las variables académicas posteriores a la matrícula presentan un riesgo de disponibilidad temporal si el objetivo fuera realizar una predicción exclusivamente al momento del ingreso. Esta situación queda documentada en el diccionario de variables.
