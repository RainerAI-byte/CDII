# Ficha del dataset

* **Dominio:** Educación superior.
* **Unidad de análisis:** Estudiante universitario.
* **Decisión apoyada:** Identificar estudiantes que requieren seguimiento y acompañamiento académico.
* **Target tentativo:** `Target`.
* **Tipo de tarea:** Clasificación multiclase.
* **Error más costoso:** Clasificar incorrectamente como no desertor a un estudiante cuyo resultado final sea `Dropout`.
* **Usuario:** Institución de educación superior, áreas de seguimiento académico y acompañamiento estudiantil.

## Pregunta del proyecto

¿Qué tan bien puede un modelo de clasificación predecir el resultado académico final de un estudiante universitario a partir de las variables disponibles?

## Fuente

**UCI Machine Learning Repository — Predict Students' Dropout and Academic Success**

El dataset contiene 4,424 instancias y 36 variables predictoras. Cada instancia representa un estudiante. El problema está formulado como clasificación de tres categorías: `Dropout`, `Enrolled` y `Graduate`.

El dataset no contiene valores faltantes y fue utilizado por sus autores con una división de 80 % para entrenamiento y 20 % para prueba.

**Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0).

**DOI:** 10.24432/C5MC89.

## Riesgo inicial de fuga de información

El dataset contiene información disponible al momento de la matrícula, pero también variables relacionadas con el rendimiento académico del primer y segundo semestre.

Por tanto, antes del entrenamiento se revisará el momento de disponibilidad de estas variables. No se eliminarán variables únicamente por su efecto sobre las métricas; cualquier exclusión deberá justificarse por disponibilidad temporal o por una razón semántica.
