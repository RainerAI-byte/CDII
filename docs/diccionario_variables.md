# Diccionario de variables

**Fuente:** UCI Machine Learning Repository — Statlog (German Credit Data).

El dataset contiene **20 variables predictoras** y una variable objetivo. Las variables predictoras son de tipo categórico o entero. El conjunto de datos no presenta valores faltantes.

| Variable    | Tipo       | Significado                                     | Unidad / codificación | Disponibilidad                  | Transformación prevista | Riesgo de fuga |
| ----------- | ---------- | ----------------------------------------------- | --------------------- | ------------------------------- | ----------------------- | -------------- |
| Attribute1  | Categórica | Estado de la cuenta corriente existente         | Categorías A11–A14    | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute2  | Entera     | Duración del crédito                            | Meses                 | Predecisión                     | Escalamiento            | Bajo           |
| Attribute3  | Categórica | Historial crediticio                            | Categorías A30–A34    | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute4  | Categórica | Propósito del crédito                           | Categorías A40–A410   | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute5  | Entera     | Monto del crédito                               | Monto monetario       | Predecisión                     | Escalamiento            | Bajo           |
| Attribute6  | Categórica | Cuenta de ahorros / bonos                       | Categorías A61–A65    | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute7  | Categórica | Tiempo en el empleo actual                      | Categorías A71–A75    | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute8  | Entera     | Tasa de la cuota respecto al ingreso disponible | Porcentaje            | Predecisión                     | Escalamiento            | Bajo           |
| Attribute9  | Categórica | Estado personal y sexo                          | Categorías A91–A95    | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute10 | Categórica | Otros deudores o garantes                       | Categorías A101–A103  | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute11 | Entera     | Tiempo de residencia actual                     | Años                  | Predecisión                     | Escalamiento            | Bajo           |
| Attribute12 | Categórica | Patrimonio / propiedad                          | Categorías A121–A124  | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute13 | Entera     | Edad                                            | Años                  | Predecisión                     | Escalamiento            | Bajo           |
| Attribute14 | Categórica | Otros planes de cuotas                          | Categorías A141–A143  | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute15 | Categórica | Vivienda                                        | Categorías A151–A153  | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute16 | Entera     | Número de créditos existentes en el banco       | Cantidad              | Predecisión                     | Escalamiento            | Bajo           |
| Attribute17 | Categórica | Tipo o calidad del empleo                       | Categorías A171–A174  | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute18 | Entera     | Personas a cargo                                | Cantidad              | Predecisión                     | Escalamiento            | Bajo           |
| Attribute19 | Categórica | Teléfono registrado a nombre del cliente        | Categorías A191–A192  | Predecisión                     | One-hot encoding        | Bajo           |
| Attribute20 | Categórica | Trabajador extranjero                           | Categorías A201–A202  | Predecisión                     | One-hot encoding        | Bajo           |
| class       | Objetivo   | Riesgo crediticio                               | 1 = Good, 2 = Bad     | Resultado que se desea predecir | Codificación del target | No aplica      |

## Observaciones sobre las variables

Las variables describen características financieras, personales y de la solicitud de crédito utilizadas para caracterizar el riesgo crediticio.

La documentación oficial de UCI identifica variables relacionadas con la duración y monto del crédito, historial crediticio, ahorros, empleo, vivienda, edad, créditos existentes y otras características del solicitante.

No se eliminarán variables únicamente por su cantidad de valores únicos. Cualquier exclusión posterior deberá estar sustentada en una razón relacionada con el significado de la variable, su disponibilidad al momento de la predicción o un riesgo documentado de fuga de información.

## Target

La variable `class` constituye el target del problema de clasificación.

* `1` = Good
* `2` = Bad

La documentación oficial de UCI confirma esta codificación. También proporciona una matriz de costos en la que clasificar como **Good** un crédito que realmente es **Bad** tiene un costo mayor que el error contrario.

## Transformaciones

Las variables numéricas se procesan mediante imputación por mediana y estandarización con `StandardScaler`.

Las variables categóricas se procesan mediante imputación por la categoría más frecuente y codificación `OneHotEncoder`.

Todo el preprocesamiento se mantiene dentro de un `Pipeline` para evitar aplicar transformaciones utilizando información del conjunto de prueba.
