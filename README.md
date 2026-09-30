# INF8239_U01 — Ciencia de Datos II

## Unidad 01

Proyecto correspondiente a la Unidad 01 de la asignatura **INF-8239 Ciencia de Datos II**.

El proyecto desarrolla un flujo reproducible para la búsqueda, selección, auditoría y clasificación de un dataset público mediante un modelo SVM.

## Dataset aprobado

El dataset utilizado en LAB02 es **Statlog (German Credit Data)**, disponible en el UCI Machine Learning Repository.

* **Fuente:** UCI Machine Learning Repository
* **Dataset:** Statlog (German Credit Data)
* **Registros:** 1,000
* **Variables predictoras:** 20
* **Variable objetivo:** `class`
* **Clases:** `1 = Good`, `2 = Bad`
* **Valores faltantes:** No
* **Tipo de variables:** categóricas e enteras
* **Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0)
* **DOI:** 10.24432/C5NC77

UCI documenta el dataset como un problema de clasificación de riesgo crediticio y proporciona información detallada sobre las variables y la matriz de costos asociada al problema.

## Fuentes

**Documentación oficial:**

https://archive.ics.uci.edu/dataset/144/statloggermancreditdata

**Descarga reproducible:**

https://archive.ics.uci.edu/static/public/144/data.csv

La descarga se encapsula en:

```text
src/inf8239_u01/data.py
```

El archivo descargado se almacena en:

```text
data/raw/dataset.csv
```

## Variable objetivo

La variable `class` representa el riesgo crediticio:

| Clase | Significado |
| ----- | ----------- |
| 1     | Good        |
| 2     | Bad         |

La distribución observada en el dataset es:

| Clase    | Registros | Porcentaje |
| -------- | --------: | ---------: |
| Good (1) |       700 |       70 % |
| Bad (2)  |       300 |       30 % |

## Auditoría

La auditoría confirmó:

* 1,000 registros.
* 21 columnas en el archivo, correspondientes a 20 predictores y el target.
* 20 variables predictoras.
* 0 valores faltantes.
* Target binario.
* Información disponible antes de la decisión crediticia.
* Sin columnas excluidas por fuga de información en esta etapa.

El detalle de las variables se encuentra en:

```text
docs/diccionario_variables.md
```

## Preprocesamiento

Las variables numéricas utilizan:

* imputación por mediana;
* estandarización mediante `StandardScaler`.

Las variables categóricas utilizan:

* imputación por la categoría más frecuente;
* `OneHotEncoder(handle_unknown="ignore")`.

El preprocesamiento se encuentra dentro de un `Pipeline` y un `ColumnTransformer`.

## División de datos

Se utiliza:

```text
Entrenamiento: 80 %
Prueba:         20 %
random_state:   42
stratify:       y
```

La misma partición se utiliza para comparar la línea base y el SVM.

## Modelos

### DummyClassifier

Se utiliza como línea base mediante la estrategia:

```text
most_frequent
```

### SVM

Se utiliza un clasificador:

```text
Kernel: RBF
C: 1
gamma: scale
probability: True
random_state: 42
```

## Resultados

| Modelo       | F1 macro |
| ------------ | -------: |
| Dummy        |   0.4118 |
| SVM base     |   0.7200 |
| SVM ajustado |   0.6855 |

El SVM base obtuvo el mejor resultado observado sobre el conjunto de prueba. La búsqueda de hiperparámetros mediante `GridSearchCV` fue utilizada como exploración y no produjo una mejora respecto al modelo base.

La mejor configuración encontrada durante la validación cruzada fue:

```text
C = 10
gamma = 0.1
CV F1 macro = 0.6688
```

Su evaluación sobre el conjunto de prueba produjo:

```text
F1 macro = 0.6855
```

## Pruebas

El proyecto incluye pruebas automatizadas para:

1. verificar que el dataset no esté vacío;
2. verificar la existencia de columnas requeridas;
3. verificar que el target no tenga valores faltantes y contenga al menos dos clases;
4. verificar que el SVM genere una predicción por cada registro;
5. verificar que el modelo produzca las clases esperadas;
6. verificar que el F1 macro se encuentre dentro del rango válido;
7. verificar el entorno del proyecto.

Ejecución:

```powershell
python -m pytest -q
```

Resultado actual:

```text
7 passed, 3 warnings
```

Las advertencias corresponden a mensajes de compatibilidad futura de `scikit-learn` y no representan fallos de las pruebas.

## Estructura del proyecto

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
│   ├── 00_verificacion.ipynb
│   ├── 01_svm_guiada.ipynb
│   └── 02_dataset_auditoria.ipynb
├── reports/
│   ├── conclusion_lab02.md
│   ├── svm_best.joblib
│   └── svm_cv_results.csv
├── src/
│   └── inf8239_u01/
│       ├── __init__.py
│       ├── data.py
│       ├── environment.py
│       └── models.py
├── tests/
│   ├── test_data_contract.py
│   ├── test_environment.py
│   └── test_models.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Notebook principal

El desarrollo de LAB02 se encuentra en:

```text
notebooks/02_dataset_auditoria.ipynb
```

El notebook documenta la descarga, carga, auditoría, definición del target, análisis de clases, preprocesamiento, partición de datos, línea base, SVM y evaluación.

## Reproducibilidad

El proyecto evita depender de rutas personales como:

```text
C:\Users\...
/content/drive
```

La fuente del dataset está documentada y la descarga se realiza mediante una función reproducible.

El objetivo es que otro usuario pueda reconstruir el dataset y ejecutar las pruebas utilizando la estructura del proyecto.
