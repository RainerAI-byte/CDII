# INF-8239 Ciencia de Datos II — Unidad 01

Proyecto correspondiente a la Unidad 01 de la asignatura **INF-8239 Ciencia de Datos II**.

El proyecto desarrolla un flujo reproducible para la selección, auditoría y clasificación de un dataset público, seguido de una comparación de modelos, reducción dimensional y análisis de costos computacionales bajo criterios de Green AI.

## Dataset aprobado

El dataset utilizado es **Statlog (German Credit Data)**, disponible en el UCI Machine Learning Repository.

* **Fuente:** UCI Machine Learning Repository
* **Dataset:** Statlog (German Credit Data)
* **Registros:** 1,000
* **Variables predictoras:** 20
* **Variable objetivo:** `class`
* **Clases:** `1 = Good`, `2 = Bad`
* **Valores faltantes:** No
* **Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0)
* **DOI:** 10.24432/C5NC77

Documentación oficial:

https://archive.ics.uci.edu/dataset/144/statloggermancreditdata

Descarga reproducible:

https://archive.ics.uci.edu/static/public/144/data.csv

El archivo descargado se almacena en:

```text
data/raw/dataset.csv
```

La descarga está encapsulada en:

```text
src/inf8239_u01/data.py
```

## Variable objetivo

La variable `class` representa el resultado de clasificación del riesgo crediticio:

| Clase | Significado |
| ----- | ----------- |
| 1     | Good        |
| 2     | Bad         |

Distribución observada:

| Clase    | Registros | Porcentaje |
| -------- | --------: | ---------: |
| Good (1) |       700 |       70 % |
| Bad (2)  |       300 |       30 % |

## Auditoría y preprocesamiento

La auditoría confirmó:

* 1,000 registros.
* 21 columnas: 20 predictores y el target.
* 0 valores faltantes.
* Target binario.
* Variables categóricas y numéricas.
* Las variables utilizadas corresponden a información disponible para la clasificación.
* No se identificaron columnas excluidas por fuga de información durante la auditoría.

Las variables numéricas utilizan:

* imputación por mediana;
* `StandardScaler`.

Las variables categóricas utilizan:

* imputación por la categoría más frecuente;
* `OneHotEncoder(handle_unknown="ignore")`.

El preprocesamiento se implementa mediante `Pipeline` y `ColumnTransformer`.

## Partición congelada

Para mantener la comparabilidad entre experimentos se utiliza la misma partición:

```text
Entrenamiento: 80 %
Prueba:        20 %
random_state:  42
stratify:      y
```

Resultado:

```text
Entrenamiento: 800 observaciones
Prueba:        200 observaciones
```

Distribución:

```text
Entrenamiento:
Clase 1 = 560
Clase 2 = 240

Prueba:
Clase 1 = 140
Clase 2 = 60
```

El conjunto de prueba permanece reservado para la evaluación final de las configuraciones.

---

# LAB02 — Línea base y SVM

Se utilizó `DummyClassifier` con estrategia `most_frequent` como línea base.

El SVM utiliza:

```text
Kernel: RBF
C: 1
gamma: scale
probability: True
random_state: 42
```

Resultados:

| Modelo       | F1 Macro |
| ------------ | -------: |
| Dummy        |   0.4118 |
| SVM base     |   0.7200 |
| SVM ajustado |   0.6855 |

La búsqueda de hiperparámetros mediante `GridSearchCV` utilizó:

```text
C = [0.1, 1, 10]
gamma = [scale, 0.01, 0.1]
CV = 5 folds estratificados
scoring = f1_macro
```

La mejor configuración durante la validación cruzada fue:

```text
C = 10
gamma = 0.1
CV F1 Macro = 0.6688
```

Su F1 Macro sobre el conjunto de prueba fue:

```text
0.6855
```

---

# LAB03 / E02 — Ensambles, reducción dimensional y Green AI

El objetivo de LAB03 es ampliar el experimento manteniendo el mismo dataset, target y partición, y comparar rendimiento predictivo con costo computacional.

La métrica principal es:

```text
F1 Macro
```

La clase de interés para el análisis es:

```text
Bad (2)
```

## Configuraciones evaluadas

Se evaluaron siete configuraciones:

1. Logistic Regression
2. SVM C=1
3. SVM C=10
4. Random Forest 100 árboles
5. Random Forest 300 árboles
6. HistGradientBoosting
7. SVM + PCA

El preprocesamiento fue homogéneo para las configuraciones comparadas.

Para permitir el uso de `HistGradientBoostingClassifier`, la salida del `OneHotEncoder` se configuró como densa mediante:

```python
OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)
```

El dataset contiene únicamente 1,000 observaciones, por lo que esta decisión permite mantener una comparación homogénea sin un costo de memoria relevante para este experimento.

## Resultados

| Modelo               | F1 Macro | Recall Macro | Ajuste mediano (s) | Inferencia (ms) | Tamaño (KB) |
| -------------------- | -------: | -----------: | -----------------: | --------------: | ----------: |
| Logistic Regression  | 0.720954 |     0.709524 |           0.088639 |         25.9600 |       7.916 |
| SVM C=1              | 0.720000 |     0.702381 |           0.404473 |         73.8966 |     268.725 |
| SVM C=10             | 0.696120 |     0.700000 |           0.792514 |         64.2953 |     277.646 |
| SVM + PCA            | 0.688150 |     0.676190 |           0.334497 |         40.3797 |     170.693 |
| HistGradientBoosting | 0.688150 |     0.676190 |           0.705587 |         38.6624 |     209.814 |
| Random Forest 100    | 0.669494 |     0.653571 |           0.752279 |         58.0897 |   1,254.636 |
| Random Forest 300    | 0.664918 |     0.650000 |           0.950452 |        221.4247 |   3,745.573 |

Cada configuración fue ajustada tres veces y se utilizó la mediana del tiempo de ajuste.

## Reducción dimensional mediante PCA

La representación después del preprocesamiento produjo:

```text
61 variables transformadas
```

La variante SVM + PCA utilizó:

```python
PCA(n_components=0.95)
```

El resultado fue:

```text
Componentes seleccionados: 32
```

Por tanto, PCA redujo la representación de 61 a 32 componentes manteniendo el objetivo de conservar el 95 % de la varianza.

## Visualización t-SNE

Se generaron dos mapas t-SNE utilizando:

```text
perplexity = 30
init = pca
learning_rate = auto
```

y dos semillas diferentes:

```text
seed = 42
seed = 7
```

Los mapas se construyeron utilizando las siete variables numéricas estandarizadas.

Los resultados se encuentran en:

```text
reports/tsne_two_seeds.png
```

t-SNE se utiliza únicamente como herramienta exploratoria de visualización. La proximidad observada en el mapa representa similitud de vecindarios en el espacio transformado y no demuestra por sí misma la existencia de grupos reales ni una relación causal.

## Frontera de Pareto

La frontera de Pareto se calculó utilizando dos criterios:

* maximizar `F1 Macro`;
* minimizar la mediana del tiempo de ajuste.

El modelo identificado como no dominado bajo estos dos criterios fue:

```text
Logistic Regression
```

La gráfica se encuentra en:

```text
reports/pareto.png
```

### Decisión cuantificada

Logistic Regression obtuvo:

```text
F1 Macro = 0.720954
```

frente a:

```text
SVM C=1 = 0.720000
```

La diferencia absoluta fue:

```text
0.000954
```

En términos de costo computacional, Logistic Regression presentó:

```text
78.09 % menos tiempo de ajuste
97.05 % menos tamaño del modelo
64.87 % menos tiempo de inferencia
```

Por tanto, bajo los criterios definidos para este experimento, Logistic Regression representa una configuración Pareto-eficiente que mantiene prácticamente el mismo F1 Macro que SVM C=1 con un costo computacional menor.

Esta conclusión está limitada al dataset, partición, hardware y configuraciones utilizadas en este experimento.

## Green AI y medición

Los tiempos corresponden a mediciones realizadas en el entorno local del proyecto.

Se midieron:

* tiempo de ajuste;
* tiempo de inferencia;
* tamaño serializado del modelo;
* F1 Macro;
* Recall Macro.

El tiempo de ejecución se utiliza como indicador operativo del costo computacional. No se presenta como medición directa de consumo eléctrico o emisiones de CO₂.

Los resultados completos se almacenan en:

```text
reports/green_ai_results.csv
```

Los modelos serializados se encuentran en:

```text
reports/models/
```

## Pruebas automatizadas

El proyecto incluye pruebas para:

* contrato del dataset;
* variables y target;
* comportamiento del SVM;
* entorno de ejecución;
* cálculo de la frontera de Pareto.

Ejecutar:

```powershell
pytest -q
```

Resultado de LAB03:

```text
9 passed, 3 warnings
```

Las advertencias corresponden a un `FutureWarning` de `scikit-learn` relacionado con `SVC(probability=True)`. No representan fallos de las pruebas y la configuración se mantiene porque forma parte del protocolo definido para el laboratorio.

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
│   ├── 02_dataset_auditoria.ipynb
│   └── 03_ensambles_reduccion_green_ai.ipynb
├── reports/
│   ├── conclusion_lab02.md
│   ├── green_ai_results.csv
│   ├── pareto.png
│   ├── svm_best.joblib
│   ├── svm_cv_results.csv
│   ├── tsne_two_seeds.png
│   └── models/
│       ├── boost.joblib
│       ├── logistic.joblib
│       ├── rf_100.joblib
│       ├── rf_300.joblib
│       ├── svm_c1.joblib
│       ├── svm_c10.joblib
│       └── svm_pca.joblib
├── src/
│   └── inf8239_u01/
│       ├── __init__.py
│       ├── data.py
│       ├── environment.py
│       ├── green.py
│       └── models.py
├── tests/
│   ├── test_data_contract.py
│   ├── test_environment.py
│   ├── test_green.py
│   └── test_models.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Reproducibilidad

El proyecto evita depender de rutas personales como:

```text
C:\Users\...
/content/drive
```

La fuente del dataset está documentada y la descarga se realiza mediante código reproducible.

La partición de datos, las semillas aleatorias, las configuraciones de modelos y las métricas utilizadas están documentadas para facilitar la repetición del experimento.

## Notebooks principales

LAB02:

```text
notebooks/02_dataset_auditoria.ipynb
```

LAB03 / E02:

```text
notebooks/03_ensambles_reduccion_green_ai.ipynb
```

El notebook de LAB03 contiene la comparación de modelos, mediciones repetidas, PCA, t-SNE, frontera de Pareto y generación de resultados.

## Archivos principales de resultados

```text
reports/green_ai_results.csv
reports/pareto.png
reports/tsne_two_seeds.png
reports/models/
```

Estos archivos constituyen las evidencias principales de la comparación realizada en E02.
