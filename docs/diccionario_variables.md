# Diccionario de variables

**Fuente:** UCI Machine Learning Repository — Predict Students' Dropout and Academic Success.

**Unidad de análisis:** estudiante universitario.

| Variable                                       | Significado                                 | Tipo / unidad                 | Disponibilidad     | Transformación prevista               | Riesgo    |
| ---------------------------------------------- | ------------------------------------------- | ----------------------------- | ------------------ | ------------------------------------- | --------- |
| Marital Status                                 | Estado civil                                | Categórica codificada         | Matrícula          | Escalado como numérica en el pipeline | Bajo      |
| Application mode                               | Modalidad de solicitud/admisión             | Categórica codificada         | Matrícula          | Escalado                              | Bajo      |
| Application order                              | Orden de preferencia de la solicitud        | Ordinal                       | Matrícula          | Escalado                              | Bajo      |
| Course                                         | Programa académico                          | Categórica codificada         | Matrícula          | Escalado                              | Bajo      |
| Daytime/evening attendance                     | Jornada de asistencia                       | Categórica binaria            | Matrícula          | Escalado                              | Bajo      |
| Previous qualification                         | Formación académica previa                  | Categórica codificada         | Matrícula          | Escalado                              | Bajo      |
| Previous qualification (grade)                 | Calificación de formación previa            | Continua, 0–200               | Matrícula          | Imputación + escalado                 | Bajo      |
| Nacionality                                    | Nacionalidad                                | Categórica codificada         | Matrícula          | Escalado                              | Bajo      |
| Mother's qualification                         | Nivel educativo de la madre                 | Categórica codificada         | Matrícula          | Escalado                              | Bajo      |
| Father's qualification                         | Nivel educativo del padre                   | Categórica codificada         | Matrícula          | Escalado                              | Bajo      |
| Mother's occupation                            | Ocupación de la madre                       | Categórica codificada         | Matrícula          | Escalado                              | Bajo      |
| Father's occupation                            | Ocupación del padre                         | Categórica codificada         | Matrícula          | Escalado                              | Bajo      |
| Admission grade                                | Calificación de admisión                    | Continua                      | Matrícula          | Imputación + escalado                 | Bajo      |
| Displaced                                      | Condición de desplazamiento                 | Binaria                       | Matrícula          | Escalado                              | Bajo      |
| Educational special needs                      | Necesidades educativas especiales           | Binaria                       | Matrícula          | Escalado                              | Bajo      |
| Debtor                                         | Condición de deudor                         | Binaria                       | Matrícula          | Escalado                              | Bajo      |
| Tuition fees up to date                        | Pagos de matrícula al día                   | Binaria                       | Matrícula          | Escalado                              | Bajo      |
| Gender                                         | Género                                      | Categórica binaria codificada | Matrícula          | Escalado                              | Bajo      |
| Scholarship holder                             | Beneficiario de beca                        | Binaria                       | Matrícula          | Escalado                              | Bajo      |
| Age at enrollment                              | Edad al ingresar                            | Años                          | Matrícula          | Imputación + escalado                 | Bajo      |
| International                                  | Estudiante internacional                    | Binaria                       | Matrícula          | Escalado                              | Bajo      |
| Curricular units 1st sem (credited)            | Asignaturas acreditadas en 1.er semestre    | Conteo                        | 1.er semestre      | Imputación + escalado                 | Medio     |
| Curricular units 1st sem (enrolled)            | Asignaturas inscritas en 1.er semestre      | Conteo                        | 1.er semestre      | Imputación + escalado                 | Medio     |
| Curricular units 1st sem (evaluations)         | Evaluaciones realizadas en 1.er semestre    | Conteo                        | 1.er semestre      | Imputación + escalado                 | Medio     |
| Curricular units 1st sem (approved)            | Asignaturas aprobadas en 1.er semestre      | Conteo                        | 1.er semestre      | Imputación + escalado                 | Medio     |
| Curricular units 1st sem (grade)               | Calificación del 1.er semestre              | Continua                      | 1.er semestre      | Imputación + escalado                 | Medio     |
| Curricular units 1st sem (without evaluations) | Asignaturas sin evaluación en 1.er semestre | Conteo                        | 1.er semestre      | Imputación + escalado                 | Medio     |
| Curricular units 2nd sem (credited)            | Asignaturas acreditadas en 2.º semestre     | Conteo                        | 2.º semestre       | Imputación + escalado                 | Alto      |
| Curricular units 2nd sem (enrolled)            | Asignaturas inscritas en 2.º semestre       | Conteo                        | 2.º semestre       | Imputación + escalado                 | Alto      |
| Curricular units 2nd sem (evaluations)         | Evaluaciones realizadas en 2.º semestre     | Conteo                        | 2.º semestre       | Imputación + escalado                 | Alto      |
| Curricular units 2nd sem (approved)            | Asignaturas aprobadas en 2.º semestre       | Conteo                        | 2.º semestre       | Imputación + escalado                 | Alto      |
| Curricular units 2nd sem (grade)               | Calificación del 2.º semestre               | Continua                      | 2.º semestre       | Imputación + escalado                 | Alto      |
| Curricular units 2nd sem (without evaluations) | Asignaturas sin evaluación en 2.º semestre  | Conteo                        | 2.º semestre       | Imputación + escalado                 | Alto      |
| Unemployment rate                              | Tasa de desempleo                           | Porcentaje                    | Contexto económico | Imputación + escalado                 | Bajo      |
| Inflation rate                                 | Tasa de inflación                           | Porcentaje                    | Contexto económico | Imputación + escalado                 | Bajo      |
| GDP                                            | Producto interno bruto                      | Indicador económico           | Contexto económico | Imputación + escalado                 | Bajo      |
| Target                                         | Resultado académico final                   | Clase                         | Resultado final    | Variable objetivo; no entra en X      | No aplica |

## Observación sobre fuga de información

Las variables correspondientes al primer y segundo semestre representan información académica posterior al momento de matrícula. UCI confirma que el dataset combina información disponible al momento de la matrícula con rendimiento académico de los dos primeros semestres.

Por esta razón, estas variables se mantienen en el experimento actual para reproducir el problema de clasificación definido por el dataset, pero se identifican como variables de **riesgo temporal** si el objetivo fuera realizar una predicción verdaderamente temprana al momento de la matrícula.

No se eliminan automáticamente porque la guía establece que toda exclusión debe estar respaldada por una justificación semántica o de disponibilidad temporal.

## Target

El target `Target` contiene tres clases:

* `Dropout`
* `Enrolled`
* `Graduate`

La documentación oficial de UCI define el problema como clasificación multiclase de tres categorías.

## Fuente y licencia

Dataset: **Predict Students' Dropout and Academic Success**.

Repositorio: UCI Machine Learning Repository.

DOI: **10.24432/C5MC89**.

Licencia: **CC BY 4.0**.
