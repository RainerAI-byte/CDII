# Model Card — SpamShield

## 1. Identificación

- Nombre: SpamShield.
- Tarea: clasificación de correos electrónicos como ham o spam.
- Tipo de modelo: aprendizaje supervisado para clasificación de texto.
- Modelos evaluados: DummyClassifier, Multinomial Naive Bayes y Regresión Logística.
- Dataset: SpamAssassin Public Corpus.
- Uso previsto: demostración académica y evaluación experimental.

## 2. Uso previsto

SpamShield permite explorar cómo los modelos de procesamiento de texto pueden ayudar a identificar correos no deseados.

El sistema no debe considerarse un filtro de correo listo para producción. Antes de un uso real serían necesarias evaluaciones con correos actuales, validación con datos independientes, controles de privacidad, pruebas de seguridad y supervisión humana.

## 3. Datos y preprocesamiento

Se utilizó un conjunto limpio de 5,897 mensajes: 4,111 ham y 1,786 spam. La partición de entrenamiento y prueba fue estratificada, 80/20, con semilla 42.

El texto se transforma mediante TF-IDF con unigramas y bigramas, minúsculas, normalización de acentos y máximo de 50,000 características.

Los datos proceden de un corpus histórico, principalmente de 2003 y 2005. La ficha del dataset documenta las decisiones de limpieza y las limitaciones conocidas.

## 4. Desempeño en el conjunto de prueba

| Indicador | Baseline | Naive Bayes | Regresión Logística |
|---|---:|---:|---:|
| Accuracy | 0.697458 | 0.924576 | 0.969492 |
| F1 Macro | 0.410884 | 0.903545 | 0.963382 |
| Precision spam | 0.000000 | 0.992647 | 0.970674 |
| Recall spam | 0.000000 | 0.756303 | 0.927171 |
| Falsos positivos | 0 | 2 | 10 |
| Falsos negativos | 357 | 87 | 26 |

Regresión Logística obtiene el mejor F1 Macro y recall de spam en esta evaluación. Naive Bayes tiene mayor precision de spam y menos falsos positivos.

Estos valores corresponden a una partición concreta y no garantizan el mismo desempeño en otras poblaciones o periodos.

## 5. Riesgos

- Falsos positivos: mensajes legítimos podrían enviarse a la carpeta de spam.
- Falsos negativos: mensajes no deseados podrían llegar a la bandeja de entrada.
- Cambio de distribución: las técnicas de spam cambian con el tiempo.
- Sesgos del corpus: los datos históricos podrían no representar idiomas, regiones, sectores o hábitos actuales.
- Señales espurias: cabeceras, firmas, citas o patrones de las fuentes pueden influir en la clasificación.
- Privacidad: los mensajes reales pueden contener información sensible y deben tratarse con controles adecuados.

## 6. Recomendaciones de uso responsable

- No eliminar correos automáticamente basándose solo en la predicción.
- Preferir cuarentena o revisión humana cuando el costo del error sea alto.
- Permitir recuperar mensajes legítimos clasificados como spam.
- Evaluar el sistema periódicamente con datos recientes y representativos.
- Registrar falsos positivos y falsos negativos para mejorar el sistema.
- No introducir información personal en servicios externos sin autorización y controles apropiados.

## 7. Limitaciones de evaluación

Se utilizó una partición aleatoria estratificada. No se realizó una validación temporal independiente ni una evaluación externa sobre correos contemporáneos.

El Average Precision del baseline refleja la prevalencia de spam debido a que sus puntuaciones no permiten discriminar entre mensajes. No debe interpretarse como capacidad efectiva de detección.

El tiempo de ejecución se registró como indicador de costo computacional; no se midió directamente el consumo eléctrico ni las emisiones de CO₂.

## 8. Artefactos

- Datos limpios: `data/processed/emails_clean.csv`.
- Modelos: `models/`.
- Comparación: `reports/results/model_comparison.csv`.
- Matrices: `reports/results/confusion_matrices.csv`.
- Métricas recalculadas: `reports/results/recomputed_metrics.csv`.
- Figura: `reports/figures/confusion_matrices.png`.
- Configuración: `reports/results/split_config.json`.

## 9. Estado

Modelo académico en fase de evaluación y documentación. No aprobado para decisiones automatizadas de producción.

