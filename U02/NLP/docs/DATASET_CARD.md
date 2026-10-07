# Dataset Card — TweetEval Sentiment

## Identificación

| Campo | Información |
|---|---|
| Nombre | TweetEval — Sentiment |
| Fuente original | CardiffNLP — TweetEval |
| Repositorio | https://github.com/cardiffnlp/tweeteval |
| Tarea | Clasificación de sentimiento |
| Idioma | Inglés |
| Registros | 59,899 |
| Variables | 3 |
| Variable objetivo | `label` |
| Licencia / términos | Según los términos aplicables al dataset y las condiciones de uso de Twitter |
| SHA-256 | `150018e6ab983bbc5991718ad996aadd32b43f483d56a0a45d59f54719be0c08` |

## Propósito y variable objetivo

El corpus se utilizará para desarrollar y evaluar modelos de clasificación automática de sentimiento dentro de la asignatura INF-8239 Ciencia de Datos II.

La variable objetivo `label` representa tres categorías de sentimiento:

- `negative`
- `neutral`
- `positive`

El texto de cada publicación se encuentra en la variable `text`.

## Diccionario de datos

| Columna | Tipo | Descripción |
|---|---|---|
| `text` | texto | Contenido textual de la publicación utilizada como entrada del modelo |
| `label` | categórica | Categoría de sentimiento: negative, neutral o positive |
| `split` | categórica | Partición original del corpus: train, val o test |

## Procedimiento de obtención

Los archivos originales de TweetEval fueron obtenidos desde el repositorio público de CardiffNLP.

Se utilizaron las tres particiones disponibles:

- `train`: 45,615 registros
- `val`: 2,000 registros
- `test`: 12,284 registros

Las particiones fueron integradas en un único archivo local:

`data/raw/dataset.csv`

El archivo contiene 59,899 registros y conserva la variable `split` para identificar la partición original de cada registro.

## Calidad observada

La auditoría automatizada produjo los siguientes resultados:

- Filas: 59,899
- Columnas: 3
- Valores nulos en `text`: 0
- Valores nulos en `label`: 0
- Textos duplicados: 28
- Longitud media del texto: 104.78 caracteres
- Longitud mediana: 111 caracteres
- Percentil 90: 138 caracteres
- Percentil 99: 150 caracteres
- Longitud máxima: 201 caracteres

La distribución observada de las clases fue:

| Clase | Proporción |
|---|---:|
| neutral | 45.88 % |
| positive | 35.13 % |
| negative | 18.99 % |

Se observa un desbalance entre las clases, particularmente una menor representación de la clase `negative`. Esta condición deberá considerarse durante la evaluación de los modelos.

Se identificaron 28 textos duplicados. No se eliminaron automáticamente durante esta etapa, debido a que la auditoría busca conservar y documentar las características observadas del corpus antes del modelado.

## Población cubierta y excluida

El corpus está compuesto por publicaciones de Twitter/X utilizadas para tareas de evaluación de lenguaje natural.

La población está limitada por las características propias de las publicaciones utilizadas en TweetEval y por el idioma inglés. Por tanto, los resultados obtenidos con este corpus no deben interpretarse automáticamente como representativos de usuarios dominicanos ni de textos escritos en español dominicano.

No se dispone, dentro de este proyecto, de información suficiente para afirmar que el corpus represente de manera uniforme todas las regiones, edades, grupos sociales o variedades lingüísticas de los usuarios de la plataforma.

## Riesgos, sesgos y usos prohibidos

Entre los principales riesgos identificados se encuentran:

1. **Desbalance de clases:** la categoría `negative` presenta una proporción menor que `neutral` y `positive`.
2. **Idioma:** el corpus está compuesto por textos en inglés, por lo que su comportamiento puede diferir significativamente en español.
3. **Contexto limitado:** el sentimiento puede depender de ironía, sarcasmo, contexto conversacional o referencias externas.
4. **Sesgo de plataforma:** los textos proceden de una plataforma específica y no representan necesariamente a la población general.
5. **Ambigüedad de lenguaje:** expresiones breves, abreviaturas y lenguaje informal pueden dificultar la clasificación.

### Usos no recomendados o prohibidos

No debe utilizarse este corpus o los modelos derivados de él para:

- tomar decisiones automatizadas de alto impacto sobre personas;
- inferir características sensibles de individuos;
- realizar vigilancia o perfilamiento individual;
- asumir que las predicciones representan correctamente el sentimiento de personas que escriben en español dominicano;
- utilizar las predicciones como única evidencia para decisiones administrativas, legales, laborales o de seguridad.

## Transformaciones realizadas

Los archivos originales de las particiones `train`, `val` y `test` fueron integrados en un archivo CSV para facilitar el procesamiento reproducible dentro del proyecto.

No se realizaron correcciones manuales de textos ni de etiquetas.

La variable `split` fue conservada para mantener la trazabilidad de la partición original.

## Decisión

**Decisión: APROBADO para el desarrollo del laboratorio y el ejercicio correspondiente.**

El corpus cumple las condiciones principales establecidas para el proyecto:

- contiene texto;
- posee una variable objetivo interpretable;
- presenta un volumen suficiente de registros;
- contiene múltiples clases;
- permite acceso reproducible;
- permite documentar su procedencia;
- permite desarrollar un clasificador de texto mediante TF-IDF y modelos supervisados.

La principal limitación identificada es que el corpus está en inglés y presenta desbalance entre clases.

## Limitaciones

Los resultados obtenidos posteriormente con este corpus deberán interpretarse dentro del contexto de TweetEval.

La calidad del modelo no implica que pueda generalizarse directamente a español, español dominicano u otros dominios textuales.

La evaluación posterior deberá considerar el desempeño por clase y no únicamente una métrica global.

## Cierre de la auditoría

**Resultado principal:** el corpus contiene 59,899 registros válidos, sin valores nulos en las variables fundamentales.

**Evidencia:** la auditoría confirmó la estructura, distribución de clases, longitud de textos, duplicados y SHA-256 del archivo.

**Riesgo principal:** desbalance de clases y diferencia lingüística respecto al contexto dominicano.

**Decisión:** aprobado.

**Próxima verificación:** evaluar el desempeño de modelos de clasificación y realizar análisis sistemático de errores en LAB05.