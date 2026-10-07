# U02.LAB06 — Conclusiones y evidencia

## 1. Resultado de embeddings

Se entrenó un modelo Word2Vec sobre el corpus público TweetEval utilizando los parámetros establecidos en el proyecto: `vector_size=60`, `window=5`, `min_count=1`, `workers=1`, `seed=42` y `epochs=30`.

El corpus procesado contiene 59,899 tweets, aproximadamente 1,061,043 tokens y 53,122 tokens únicos. El modelo obtuvo un vocabulario de 53,122 términos y una cobertura de 1.000.

La palabra seleccionada para el análisis fue `tomorrow`, debido a que estaba presente en el vocabulario. Sus vecinos más próximos con `window=5` fueron:

| Vecino    | Similitud |
| --------- | --------: |
| monday    |    0.6501 |
| saturday  |    0.6463 |
| thursday  |    0.6307 |
| friday    |    0.6243 |
| wednesday |    0.6189 |
| tuesday   |    0.6047 |
| tonight   |    0.5770 |
| sunday    |    0.5704 |
| thurs     |    0.5590 |
| wed       |    0.5090 |

Los resultados muestran proximidad contextual entre `tomorrow` y términos relacionados principalmente con referencias temporales. Esta similitud debe interpretarse como una regularidad aprendida del corpus y no como sinonimia universal.

## 2. Experimento de parámetro

Se compararon dos configuraciones modificando únicamente el parámetro `window`.

| Configuración | Vocabulario | Cobertura | Observación                                             |
| ------------- | ----------: | --------: | ------------------------------------------------------- |
| `window=5`    |      53,122 |     1.000 | Configuración base                                      |
| `window=10`   |      53,122 |     1.000 | Cambiaron las similitudes y el orden de algunos vecinos |

Con `window=10`, las similitudes de los vecinos principales aumentaron y se observaron cambios en el orden de los términos cercanos. La cobertura y el tamaño del vocabulario permanecieron iguales porque no se modificó `min_count`.

El experimento muestra que ampliar la ventana permite incorporar un contexto más amplio alrededor de cada palabra y puede modificar las relaciones vectoriales aprendidas.

Después del experimento se restauró `window=5`, manteniendo la configuración base indicada en el proyecto.

## 3. Resultado de la red

Se utilizó la red de demostración del Zachary Karate Club.

Los resultados obtenidos fueron:

* **Nodos:** 34
* **Aristas:** 78
* **Comunidades:** 3
* **Modularidad:** 0.411

El análisis generó los siguientes archivos:

* `reports/centralities.csv`
* `reports/network.png`
* `reports/social_network.graphml`

La modularidad de 0.411 describe la separación estructural de la partición de comunidades encontrada por el algoritmo. No debe interpretarse como evidencia de que existan exactamente tres grupos sociales reales fuera de esta red de demostración.

## 4. Comparación de centralidades

Se compararon centralidad de grado, intermediación y PageRank.

El nodo 33 presentó la mayor centralidad de grado, con **0.5152**, mientras que el nodo 0 presentó la mayor centralidad de intermediación, con **0.4376**. El nodo 33 también presentó el mayor PageRank, con **0.0970**.

La diferencia entre las métricas demuestra que cada medida describe una propiedad estructural diferente. La centralidad de grado representa la cantidad relativa de conexiones directas; la intermediación refleja la participación del nodo en caminos mínimos; y PageRank considera la importancia estructural de los nodos que enlazan con él.

## 5. Interpretación responsable

Los embeddings permiten estudiar proximidad contextual entre palabras dentro del corpus utilizado. Las centralidades permiten describir propiedades estructurales de los nodos de una red determinada.

No es válido afirmar que dos palabras son sinónimas únicamente porque presenten una similitud vectorial elevada.

Tampoco es válido afirmar que un nodo representa a la persona más influyente únicamente porque tenga una centralidad elevada. En esta demostración, los nodos representan elementos de una red abstracta y las métricas describen propiedades estructurales de esa red.

## 6. Limitaciones

El corpus TweetEval utilizado para esta práctica está compuesto por textos en inglés. Por esta razón, los resultados no deben extrapolarse directamente a mensajes dominicanos en español.

Los embeddings dependen del corpus, la tokenización y los parámetros utilizados. Asimismo, los resultados de la red dependen de cómo se definan los nodos, las aristas y las métricas.

La red del Karate Club es una demostración reproducible y no contiene información suficiente para establecer influencia causal, identidad social o características personales.

## 7. Verificación

La prueba específica de LAB06 fue ejecutada correctamente:

```text
2 passed
```

También se verificó la generación de los tres artefactos requeridos:

```text
reports/centralities.csv
reports/network.png
reports/social_network.graphml
```

## 8. Conclusión

LAB06 permitió complementar la clasificación de texto desarrollada anteriormente con dos formas diferentes de analizar relaciones: representaciones vectoriales mediante embeddings y estructura mediante análisis de redes.

El modelo Word2Vec obtuvo una cobertura completa sobre los tokens procesados y mostró relaciones contextuales coherentes alrededor de `tomorrow`. El experimento con `window=10` demostró que ampliar el contexto modifica las similitudes aprendidas, aunque en este caso no cambió el vocabulario ni la cobertura.

El análisis de la red identificó tres comunidades y mostró que las distintas métricas de centralidad pueden producir resultados diferentes. Por tanto, la interpretación debe estar vinculada siempre a la propiedad matemática que mide cada métrica y al diseño de la red.

Como siguiente experimento se propone continuar evaluando otras palabras del corpus o comparar de forma controlada `window` y `min_count`, manteniendo constantes los demás parámetros y documentando los cambios observados.
