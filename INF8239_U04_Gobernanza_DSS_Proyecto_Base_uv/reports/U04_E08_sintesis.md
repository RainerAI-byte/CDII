# U04.E08 — Expediente de gobernanza y DSS responsable

**Asignatura:** INF-8239 Ciencia de Datos II  
**Unidad:** 04 — Ética y Roles en Ciencia de Datos  
**Sistema:** Territorial Review DSS — Synthetic  
**Decisión humana:** REVIEW — despliegue real no autorizado  
**Repositorio:** https://github.com/RainerAI-byte/CDII/tree/master/INF8239_U04_Gobernanza_DSS_Proyecto_Base_uv

## 1. Resumen ejecutivo

Este expediente integra la documentación de gobernanza, evaluación de equidad, responsabilidades, respuesta a incidentes y uso de herramientas de inteligencia artificial del proyecto U04.E08.

El sistema se utiliza exclusivamente con datos sintéticos y para fines académicos. La salida automática de los controles de LAB13 no constituye una aprobación institucional ni sustituye la decisión humana.

La decisión final es REVIEW. No se autoriza el despliegue real, la intervención automática ni la adopción de decisiones reales sobre personas basadas únicamente en las predicciones.

## 2. Datos, inventario y minimización

El conjunto `data/territorial_risk_synthetic.csv` contiene 640 observaciones y 9 columnas, según la documentación del proyecto. Los datos son sintéticos y no representan personas, ubicaciones, tasas ni estadísticas oficiales de República Dominicana.

La ficha del dataset documenta finalidad, procedencia, usos prohibidos, limitaciones y trazabilidad. El inventario y la política de conservación se describen en `docs/DATA_INVENTORY_RETENTION.md`.

La variable `protected_group` se reserva para auditoría de equidad y no debe emplearse como predictor. `age_band` se trata como dimensión sensible para el análisis de subgrupos.

Antes de utilizar datos reales deberán evaluarse necesidad, proporcionalidad, finalidad, minimización, permisos de acceso, seguridad, conservación y eliminación. No se deben incorporar identificadores personales sin una justificación y autorización apropiadas.

## 3. Modelo y evaluación

Se compararon Logistic Regression y Tree sobre 160 casos de evaluación, utilizando las métricas documentadas en `reports/lab12/`.

### Logistic Regression

- Exactitud: 0.71875.
- Recall de la clase positiva: 0.71739.
- Diferencia de recall entre grupos: 0.13764.
- Diferencia de FPR entre grupos: 0.125.
- Tamaño serializado: aproximadamente 3.56 KB.

El modelo satisface los umbrales agregados configurados: recall mínimo de 0.68, diferencia máxima de recall de 0.16 y diferencia máxima de FPR de 0.16.

Sin embargo, el cumplimiento de estos umbrales no demuestra equidad integral. La auditoría interseccional identifica subgrupos con recall inferior a 0.68. Además, la diferencia de tasas de selección entre grupos es aproximadamente 0.2324, por lo que debe investigarse aunque no exista un umbral configurado para esa métrica.

### Tree

- Exactitud: 0.70625.
- Recall de la clase positiva: 0.71739.
- Diferencia de recall entre grupos: 0.18130.
- Diferencia de FPR entre grupos: 0.16827.
- Tamaño serializado: aproximadamente 7.87 KB.

Tree incumple los límites configurados para las diferencias de recall y FPR. El incidente simulado documenta la detección, contención, preservación de evidencia, comunicación, reversión y acciones posteriores.

### Interpretación

Los resultados proceden de un conjunto sintético y de muestras de tamaño limitado. Las diferencias observadas sirven para identificar cuestiones que requieren investigación; no demuestran discriminación causal ni permiten generalizar el desempeño a poblaciones reales.

No se ha medido directamente el consumo eléctrico ni las emisiones de carbono.

## 4. Decisión de gobernanza

**Decisión final: REVIEW. Despliegue real no autorizado.**

La decisión automática y la decisión humana se conservan por separado:

- `reports/lab13/deployment_decision_automatic.json`: salida automática de los controles.
- `reports/lab13/deployment_decision.json`: registro de la decisión con revisión humana.

Aunque Logistic Regression cumple los umbrales agregados configurados, persisten limitaciones interseccionales y no se ha demostrado validez para poblaciones reales. La decisión responsable es mantener el proyecto en el ámbito académico.

### Condiciones para reconsiderar la decisión

1. Investigar los subgrupos con recall inferior a 0.68.
2. Revisar las diferencias de tasas de selección y otras métricas relevantes.
3. Documentar incertidumbre y limitaciones de las muestras pequeñas.
4. Repetir las auditorías y pruebas después de cambios en datos, código o modelos.
5. Evaluar privacidad, calidad, finalidad y proporcionalidad antes de considerar datos reales.
6. Obtener revisión humana documentada y la autorización institucional correspondiente.

## 5. Responsabilidades y traspaso

La matriz `docs/RACI_HANDOFF.md` y `student_inputs/raci.csv` documentan la asignación propuesta de responsabilidades.

La matriz es una propuesta académica y no representa una asignación oficial de cargos dentro de la UASD. Antes de una implementación institucional, los responsables deberán ser designados formalmente.

El traspaso entre desarrollo, auditoría, operación y responsables institucionales debe incluir versión, métricas, limitaciones, evidencia, incidentes abiertos y decisión vigente.

## 6. Monitoreo, runbook e incidentes

El procedimiento operativo se documenta en `docs/RUNBOOK.md`. Incluye verificaciones, controles de operación y pautas de respuesta.

El postmortem `reports/lab13/INCIDENT_POSTMORTEM.md` registra el escenario en el que Tree incumple los controles de equidad configurados. La respuesta contempla:

- Detectar y registrar el incumplimiento.
- Contener el sistema y detener el uso de la versión afectada.
- Preservar métricas, configuración, código y evidencias.
- Comunicar el incidente a los responsables correspondientes.
- Revertir a revisión manual sin automatización.
- Definir acciones correctivas, responsables y criterios de recuperación.
- Repetir pruebas y auditorías antes de reconsiderar el uso.

Los plazos y responsables que estén pendientes deberán asignarse expresamente; no deben considerarse completados por el mero hecho de aparecer en un documento.

## 7. Obligaciones, marcos voluntarios y recomendaciones

### Obligaciones legales

La aplicabilidad de la normativa dominicana de protección de datos y de las reglas administrativas pertinentes debe determinarse antes de cualquier tratamiento de datos personales o implementación real. La presencia de datos sintéticos en este ejercicio no demuestra por sí misma el cumplimiento de requisitos legales aplicables a otro contexto.

Las obligaciones concretas, la base jurídica, los derechos de los titulares, los plazos de conservación y los requisitos de autorización deberán verificarse con fuentes oficiales y asesoría competente antes de un despliegue.

### Marcos voluntarios

Los marcos de gestión de riesgos de IA, como NIST AI RMF, pueden servir como referencias voluntarias para estructurar identificación, evaluación, seguimiento y tratamiento de riesgos. No deben presentarse como leyes dominicanas ni como obligaciones legales automáticas.

### Recomendaciones éticas e institucionales

Se recomienda mantener supervisión humana, documentar la incertidumbre, revisar los impactos por grupo, minimizar los datos y prohibir decisiones automáticas mientras no exista evidencia suficiente y autorización formal.

Estas recomendaciones deben distinguirse de las obligaciones legales verificadas y de las políticas internas formalmente aprobadas.

## 8. Uso de herramientas de inteligencia artificial

La declaración `docs/U04_E08_AI_USE_DECLARATION.md` describe el apoyo de ChatGPT en la organización del expediente, la redacción de borradores, la interpretación de métricas y la preparación de verificaciones.

Los valores numéricos deben contrastarse con los archivos de resultados del proyecto. La salida automática GO de LAB13 no se considera aprobación humana. No se atribuyen mediciones de energía o carbono que no se hayan realizado.

El estudiante conserva la responsabilidad de verificar las afirmaciones, corregir errores, validar referencias y defender la decisión final. La declaración deberá ajustarse si no refleja fielmente el uso real de herramientas.

## 9. Evidencias y reproducibilidad

Artefactos principales:

- `docs/DATASET_CARD.md`
- `docs/DATA_INVENTORY_RETENTION.md`
- `docs/MODEL_CARD.md`
- `docs/RUNBOOK.md`
- `docs/RACI_HANDOFF.md`
- `docs/AI_USE_DECLARATION.md`
- `docs/U04_E08_DECISION_RECORD.md`
- `reports/lab13/deployment_decision.json`
- `reports/lab13/deployment_decision_automatic.json`
- `reports/lab13/INCIDENT_POSTMORTEM.md`
- `student_inputs/raci.csv`
- `student_inputs/lab12_decision.yml`

La ejecución registrada de `uv run pytest -q` produjo 10 pruebas aprobadas. Debe repetirse antes de la entrega final para confirmar el estado actual del proyecto.

## 10. Conclusión

La evaluación demuestra que cumplir umbrales agregados no basta para autorizar el uso real de un sistema de apoyo a decisiones. Las limitaciones interseccionales, la incertidumbre de las muestras y la ausencia de validación en poblaciones reales justifican mantener la decisión REVIEW.

El proyecto queda restringido al uso académico con datos sintéticos y revisión humana. Cualquier reconsideración exige nueva evidencia, auditoría documentada, corrección de hallazgos y autorización formal.
