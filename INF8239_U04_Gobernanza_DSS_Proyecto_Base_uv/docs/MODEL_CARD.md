# Model Card — Territorial Review DSS — Synthetic

**Asignatura:** INF-8239 Ciencia de Datos II  
**Unidad:** 04 — Ética y Roles en Ciencia de Datos  
**Sistema:** Territorial Review DSS — Synthetic  
**Modelo evaluado:** Logistic Regression  
**Estado de gobernanza:** REVIEW  
**Autorización de despliegue operativo:** No autorizada

## 1. Uso previsto

Modelo experimental de clasificación para practicar evaluación predictiva, auditoría de equidad, trazabilidad y gobernanza responsable con datos sintéticos.

La salida puede utilizarse exclusivamente como ejemplo académico de una recomendación que requiere revisión humana. No constituye una decisión definitiva.

## 2. Usos fuera de alcance

Se prohíbe utilizar el sistema para:

- Tomar decisiones automáticas sobre personas.
- Determinar elegibilidad para servicios, beneficios o recursos.
- Ordenar intervenciones reales o declarar emergencias.
- Perfilar personas o comunidades reales.
- Procesar datos personales reales en el marco de este ejercicio.
- Presentar sus resultados como estadísticas oficiales de la República Dominicana.

## 3. Datos y evaluación

El proyecto utiliza un conjunto de datos sintético y educativo. La comprobación del entorno registró 640 filas y 9 columnas.

En la ejecución evaluada por LAB12 se reportaron 160 casos. La partición registrada en el proyecto debe consultarse en el código para confirmar los detalles completos de entrenamiento, prueba y estratificación.

Las etiquetas `protected_group` y `age_band` se emplean para analizar diferencias entre grupos. Su utilización en auditoría no implica que sean una justificación suficiente para decidir sobre casos individuales.

**Fuente de trazabilidad:** dataset del proyecto U04, código de LAB12, configuración de gobernanza y archivos de resultados.

## 4. Resultados globales

Resultados registrados para Logistic Regression:

| Métrica | Resultado |
|---|---:|
| Casos evaluados | 160 |
| Accuracy | 71.88 % |
| Recall global | 71.74 % |
| Recall mínimo configurado | 68.00 % |
| Brecha de recall entre grupos | 13.76 puntos porcentuales |
| Brecha de FPR entre grupos | 12.50 puntos porcentuales |
| Brecha de tasa de selección | 23.24 puntos porcentuales |
| Tamaño del modelo | 3.56 KB |
| Tiempo de entrenamiento registrado por LAB12 | 0.048 segundos |

El tiempo de entrenamiento informado por LAB13 fue de aproximadamente 0.053 segundos. La diferencia entre mediciones debe conservarse como parte de la trazabilidad de cada ejecución; no se debe presentar como si ambas fueran una única medición idéntica.

## 5. Evaluación por grupos e intersecciones

La auditoría interseccional de LAB12 registró los siguientes resultados:

| Grupo sintético | Casos | Recall | Umbral mínimo | Cumplimiento |
|---|---:|---:|---:|---|
| G1, 18–29 | 18 | 75.00 % | 68.00 % | Sí |
| G1, 30–44 | 24 | 56.25 % | 68.00 % | No |
| G1, 45–59 | 35 | 58.82 % | 68.00 % | No |
| G1, 60+ | 24 | 83.33 % | 68.00 % | Sí |
| G2, 18–29 | 11 | 87.50 % | 68.00 % | Sí |
| G2, 30–44 | 14 | 66.67 % | 68.00 % | No |
| G2, 45–59 | 8 | 100.00 % | 68.00 % | Sí |
| G2, 60+ | 26 | 76.47 % | 68.00 % | Sí |

Las diferencias interseccionales muestran que un resultado global aceptable puede ocultar un desempeño insuficiente en determinados segmentos. Los grupos con pocos casos, como G2 de 45–59 años, requieren especial cautela: una métrica alta en una muestra pequeña no demuestra un desempeño estable.

Los resultados corresponden únicamente al conjunto sintético del experimento y no permiten inferir el comportamiento del modelo en poblaciones reales.

## 6. Evidencia Green AI

El proyecto registra indicadores operacionales de costo computacional:

- Tiempo de entrenamiento.
- Tamaño del modelo serializado.
- Latencia de inferencia.

En LAB13 se registraron aproximadamente 0.053 segundos de entrenamiento, 3.56 KB de tamaño y 0.045 milisegundos de latencia.

Estos indicadores no equivalen a una medición directa del consumo eléctrico ni de las emisiones de carbono.

## 7. Limitaciones y supervisión humana

- El conjunto de datos es sintético y no representa la distribución de una población real.
- El resultado depende de los datos, el preprocesamiento, la partición y la configuración experimental.
- Las métricas globales no bastan para evaluar equidad.
- Las diferencias observadas deben investigarse antes de considerar cambios de alcance.
- No se ha demostrado que el modelo sea apto para uso operativo.
- El análisis no constituye una certificación de ausencia de sesgo ni de cumplimiento legal.

La revisión humana debe poder rechazar la recomendación, documentar la razón y solicitar una nueva evaluación. Toda desviación relevante debe registrarse y escalarse al responsable del ejercicio.

## 8. Decisión de gobernanza

El control automático de LAB13 produjo `GO` en sus cinco comprobaciones configuradas. Sin embargo, los resultados interseccionales incluyen recalls inferiores al umbral mínimo de 68 %.

**Decisión humana: REVIEW.**

**Despliegue operativo: no autorizado.**

El uso queda limitado a datos sintéticos y fines académicos. Antes de reconsiderar la decisión, se requiere investigar las diferencias interseccionales, documentar acciones correctivas y evaluar nuevamente los resultados mediante un protocolo reproducible.

## 9. Responsabilidad y revisión

**Responsable institucional:** pendiente de designación formal para el ejercicio.  
**Equipo técnico:** responsable de documentar código, métricas, pruebas y limitaciones.  
**Revisor humano:** responsable de examinar las alertas y registrar observaciones.  
**Fecha de revisión:** pendiente de registrar.

Esta ficha debe actualizarse cuando cambien el modelo, los datos, el protocolo de evaluación o la decisión de gobernanza.

## 10. Artefactos de respaldo

- `docs/DATASET_CARD.md`
- `docs/DATA_INVENTORY_RETENTION.md`
- `docs/RUNBOOK.md`
- `configs/governance.yml`
- `reports/lab12/logistic/global_metrics.json`
- `reports/lab12/logistic/fairness_by_group.csv`
- `reports/lab12/logistic/fairness_intersectional.csv`
- `reports/lab13/deployment_decision.json`
- `reports/lab11/DECISION_RECORD.md`

