# INF-8239 Â· Unidad 02 Â· Proyecto NLP

Autor acadÃ©mico: Edwin RamÃ³n JosÃ© Nolasco

Proyecto base para LAB04â€“LAB06. No sustituya la comprensiÃ³n por ejecuciÃ³n mecÃ¡nica.

## Inicio rÃ¡pido

```bash
uv python install 3.12
uv sync
uv run pytest -q
uv run python scripts/audit_data.py
```

Copie `.env.example` como `.env` y configure el dataset aprobado.

## Dataset

Complete `docs/DATASET_CARD.md`, el diccionario, la licencia y el procedimiento de obtenciÃ³n.
El archivo `data/sample/demo_text.csv` solamente comprueba la arquitectura.

## Entrenamiento

```bash
uv run python scripts/train_text.py
uv run streamlit run app/streamlit_app.py
```

## InterpretaciÃ³n

Toda conclusiÃ³n debe separar observaciÃ³n, evidencia, interpretaciÃ³n y decisiÃ³n.
## Cierre interpretativo

**Resultado principal:**  
Se desarrolló y evaluó un clasificador de sentimiento utilizando el corpus público TweetEval Sentiment. El conjunto contiene 59,899 textos en inglés distribuidos en las clases negative, neutral y positive. Se compararon tres alternativas: DummyClassifier como línea base, Complement Naive Bayes y Regresión Logística. Los resultados muestran una diferencia clara entre los modelos. DummyClassifier obtuvo un F1 macro de 0.2096, Complement Naive Bayes alcanzó 0.5532 y Regresión Logística obtuvo el mejor resultado con 0.6461.

**Modelo seleccionado y evidencia:**  
Se selecciona **Regresión Logística** como modelo final del ejercicio porque presentó el mayor F1 macro. La diferencia respecto a Complement Naive Bayes fue de aproximadamente 0.093 puntos de F1 macro, mientras que frente a DummyClassifier fue de aproximadamente 0.436 puntos. Esta mejora indica que el modelo aprendió patrones útiles para distinguir las clases de sentimiento del corpus. La evidencia cuantitativa se encuentra en `reports/text_metrics.csv`, mientras que `reports/confusion_text.png` permite observar la distribución de las predicciones correctas e incorrectas. El modelo final fue almacenado en `models/text_model.joblib`.

**Clase con mayor dificultad:**  
La clase **negative** presentó la mayor dificultad relativa. Para esta clase, la Regresión Logística obtuvo aproximadamente 0.59 de F1, frente a 0.64 para neutral y 0.71 para positive. Este resultado indica que las expresiones negativas fueron más difíciles de identificar correctamente que las positivas y neutrales. La diferencia puede estar relacionada con la variedad de formas lingüísticas utilizadas para expresar una valoración negativa.

**Tipo de error más frecuente:**  
En los errores revisados se identificaron casos relacionados con ambigüedad, falta de contexto, ironía, expresiones cortas, dialecto o lenguaje contextual, etiquetas cuestionables y contenido fuera del dominio. No todos los errores pueden atribuirse exclusivamente al algoritmo. Algunos textos requieren información adicional o conocimiento externo para determinar correctamente el sentimiento. Por esta razón, la revisión cualitativa de errores complementa la evaluación numérica.

**Impacto en el contexto:**  
El modelo resulta apropiado como demostración académica de clasificación automática de sentimiento y permite observar cómo una representación TF-IDF combinada con modelos supervisados puede resolver una tarea de procesamiento de lenguaje natural. Sin embargo, una predicción incorrecta puede conducir a una interpretación equivocada del sentimiento expresado. Esto es especialmente relevante cuando el texto contiene sarcasmo, ironía, referencias culturales o significados dependientes del contexto.

**Limitación del dataset:**  
La principal limitación es que TweetEval Sentiment utiliza textos en inglés procedentes del dominio de Twitter/X. Por tanto, el modelo no debe interpretarse como un clasificador general de sentimiento para cualquier idioma, población o dominio. La prueba realizada con la expresión en español `te odio`, clasificada como `neutral`, evidencia esta limitación de dominio lingüístico. También debe considerarse que los textos de redes sociales presentan características particulares de vocabulario, abreviaciones, emojis y referencias contextuales.

**Decisión antes del despliegue:**  
Se aprueba la **Regresión Logística** como modelo final para el propósito académico establecido. El modelo queda disponible para demostraciones y pruebas controladas mediante la aplicación Streamlit. No se recomienda utilizarlo directamente en producción ni para decisiones de alto impacto sin una validación adicional con datos representativos del contexto objetivo. Si el sistema fuera destinado a textos en español, sería necesario utilizar o construir un corpus adecuado en español y repetir la evaluación. Antes de un eventual despliegue también deberían revisarse desempeño por clase, sesgos, estabilidad y comportamiento frente a datos fuera de distribución.

En conclusión, el ejercicio demuestra que la selección del modelo debe sustentarse tanto en métricas cuantitativas como en la revisión cualitativa de errores. La Regresión Logística ofrece el mejor desempeño entre las alternativas evaluadas, pero sus resultados deben interpretarse dentro de las características y limitaciones del corpus utilizado.
## Evidencia del Ejercicio 03

- README actualizado.
- Auditoría del dataset.
- Métricas comparativas.
- Matriz de confusión.
- Análisis de al menos 20 errores categorizados.
- Pruebas automatizadas.
- Modelo entrenado.
- Aplicación Streamlit local.
- Preparación para despliegue mediante `requirements-cloud.txt`.
- Conclusión interpretativa.

## Archivos principales

- `docs/DATASET_CARD.md`
- `reports/text_metrics.csv`
- `reports/confusion_text.png`
- `reports/error_analysis.csv`
- `models/text_model.joblib`
- `app/streamlit_app.py`
- `requirements-cloud.txt`

