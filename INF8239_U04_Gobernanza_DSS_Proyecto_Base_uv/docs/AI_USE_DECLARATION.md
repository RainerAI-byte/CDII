# Declaración de uso de inteligencia artificial

**Asignatura:** INF-8239 Ciencia de Datos II  
**Unidad:** 04 — Ética y Roles en Ciencia de Datos  
**Ejercicio:** U04.E08 — Expediente de gobernanza y simulacro  
**Proyecto:** Territorial Review DSS — Synthetic

## 1. Herramientas utilizadas

Se utilizó ChatGPT como herramienta de apoyo durante la organización del expediente, la estructuración de documentos técnicos, la revisión de coherencia entre los resultados y las decisiones de gobernanza, y la preparación de propuestas de documentación.

La herramienta se utilizó como asistente de redacción y análisis, no como sustituto de las responsabilidades del estudiante.

## 2. Finalidades del uso

La asistencia de IA se empleó para:

- Organizar la documentación según los criterios de la rúbrica de U04.E08.
- Proponer estructuras para el inventario de datos, la matriz RACI y el registro del simulacro.
- Mejorar la claridad y consistencia de la Model Card y otros documentos.
- Identificar discrepancias que requieren verificación entre el resultado automático de LAB13 y la decisión humana de gobernanza.
- Proponer comandos de PowerShell para inspeccionar archivos y comprobar el estado de los artefactos.
- Elaborar explicaciones sobre limitaciones, supervisión humana y trazabilidad.

## 3. Prompts relevantes

Los prompts relevantes incluyeron solicitudes para:

1. Organizar las evidencias de LAB11, LAB12 y LAB13 de acuerdo con los criterios de U04.E08.
2. Elaborar un inventario de datos con minimización, acceso y retención.
3. Preparar una matriz RACI y un protocolo de traspaso entre roles.
4. Diseñar un simulacro académico basado en las brechas de recall observadas.
5. Revisar la ficha del modelo y distinguir los resultados automáticos de la decisión humana.
6. Verificar qué artefactos existen antes de afirmar que la entrega está completa.

Estos prompts se resumen por su finalidad; no se presentan como transcripciones literales completas de cada interacción.

## 4. Verificaciones humanas y técnicas

La documentación se contrastó con los resultados y archivos del proyecto cuando estuvieron disponibles. Entre las verificaciones registradas se encuentran:

- Inspección de la estructura de carpetas mediante PowerShell.
- Lectura de los resultados de LAB12 y LAB13.
- Contraste de las métricas por grupo con el umbral de recall configurado.
- Revisión de la diferencia entre el estado automático `GO` y la decisión humana `REVIEW`.
- Identificación de archivos incompletos que aún contenían marcadores `REPLACE`.
- Reconocimiento de que la carpeta U04 no es un repositorio Git independiente.

La existencia de un archivo o la redacción de un procedimiento no demuestra por sí sola que todas las pruebas, acciones correctivas o actividades de simulación se hayan ejecutado.

## 5. Errores, limitaciones y correcciones

Durante la preparación del expediente se identificaron las siguientes situaciones:

- La primera propuesta del simulacro describía un procedimiento, pero no constituía evidencia de ejecución. Se estableció la necesidad de registrar las acciones efectivamente realizadas.
- `docs/MODEL_CARD.md` contenía secciones sin completar. Se preparó una versión desarrollada a partir de las métricas registradas.
- `docs/AI_USE_DECLARATION.md` contenía un marcador pendiente de reemplazo.
- `reports/lab11/DECISION_RECORD.md` contenía información de tipo Model Card, por lo que se identificó la necesidad de evitar duplicaciones y mantener trazabilidad.
- `reports/lab13/deployment_decision.json` registraba la decisión automática, pero debía verificarse e incorporar por separado la revisión humana acordada.

Las correcciones documentales deben verificarse en los archivos guardados. No se declara que todos estos puntos estén resueltos hasta completar la comprobación final.

## 6. Responsabilidad del estudiante

El estudiante es responsable de:

- Comprender y defender las métricas, las decisiones y las limitaciones.
- Verificar las referencias y cualquier interpretación normativa incluida en el informe.
- Comprobar el código y ejecutar las pruebas requeridas.
- Diferenciar los resultados observados de las propuestas redactadas con ayuda de IA.
- No inventar evidencias, resultados, firmas, aprobaciones ni incidentes.
- Confirmar que los artefactos publicados correspondan al proyecto y puedan inspeccionarse.

## 7. Conclusión

La inteligencia artificial se utilizó como herramienta auxiliar de organización, redacción y revisión. Los resultados cuantitativos se vinculan con los archivos de ejecución del proyecto y las decisiones de gobernanza deben ser revisadas y asumidas por el estudiante.

Esta declaración debe actualizarse si se incorporan nuevas herramientas, prompts, verificaciones o correcciones durante la finalización de la entrega.
