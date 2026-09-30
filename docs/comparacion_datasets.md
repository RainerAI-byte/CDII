# Comparación de candidatos

| Criterio           | Candidato A: Predict Students' Dropout                                        | Candidato B: Iranian Churn                        |
| ------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------- |
| Procedencia        | UCI Machine Learning Repository                                               | UCI Machine Learning Repository                   |
| Licencia           | CC BY 4.0                                                                     | CC BY 4.0                                         |
| Filas              | 4,424                                                                         | 3,150                                             |
| Columnas/variables | 36 predictoras + target                                                       | 13 predictoras + target                           |
| Tipo de tarea      | Clasificación multiclase                                                      | Clasificación binaria                             |
| Target             | `Target`                                                                      | `Churn`                                           |
| Clases             | Dropout, Enrolled, Graduate                                                   | Churn, Non-churn                                  |
| Valores ausentes   | No                                                                            | No                                                |
| Unidad de análisis | Estudiante                                                                    | Cliente                                           |
| Riesgo de fuga     | Alto si se usan variables de rendimiento posteriores al momento de predicción | Bajo, debido a la separación temporal documentada |
| Tamaño para CPU    | Compatible                                                                    | Compatible                                        |
| Aplicación         | Seguimiento académico y abandono universitario                                | Retención de clientes                             |
| Documentación      | UCI + diccionario de variables                                                | UCI + diccionario de variables                    |

## Decisión

Se propone utilizar **Predict Students' Dropout and Academic Success** para el desarrollo del laboratorio.

La selección responde principalmente a la posibilidad de formular una pregunta institucional relacionada con educación superior y a que el dataset fue creado específicamente para estudiar el abandono y éxito académico mediante modelos de clasificación.

El principal riesgo identificado es el posible data leakage asociado con las variables de rendimiento del primer y segundo semestre. Por tanto, antes del entrenamiento se documentará el momento de predicción y se justificará cualquier variable excluida.

El dataset Iranian Churn se mantiene como candidato alternativo y cumple los criterios mínimos de tamaño, clasificación, documentación, licencia y ausencia de valores faltantes.
