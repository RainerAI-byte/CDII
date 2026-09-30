# Ficha del dataset

## Dataset

**Statlog (German Credit Data)**

## Dominio

Evaluación y clasificación del riesgo crediticio.

## Unidad de análisis

Cada registro representa una solicitud de crédito correspondiente a una persona solicitante.

## Decisión

Determinar la clasificación de riesgo crediticio de una solicitud como **Good** o **Bad**.

## Target

La variable objetivo es `class`, que representa la clasificación del crédito.

* `Good`: crédito clasificado como bueno.
* `Bad`: crédito clasificado como malo.

## Error más costoso

El error de mayor impacto para la institución financiera sería clasificar como **Good** una solicitud que realmente pertenece a la clase **Bad**, debido a que podría aprobarse o considerarse favorable una operación asociada con un mayor riesgo de incumplimiento.

## Usuario

El usuario del modelo sería el área responsable de evaluación y aprobación de créditos de una entidad financiera.

## Pregunta de modelado

¿Es posible utilizar las características disponibles de una solicitud de crédito para clasificar su riesgo como **Good** o **Bad**?
