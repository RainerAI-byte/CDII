# Dataset Card — Territorial Review DSS (Synthetic)

## 1. Identificación y procedencia

- **Nombre:** Territorial Review DSS — Synthetic.
- **Tipo:** conjunto de datos sintético, generado para fines académicos.
- **Archivo principal:** `data/territorial_risk_synthetic.csv`.
- **Tamaño documentado:** 640 observaciones y 9 columnas.
- **Generación:** datos artificiales con una semilla fija para facilitar la reproducibilidad.
- **Representatividad:** no representa personas, ubicaciones, tasas ni estadísticas oficiales de República Dominicana.

## 2. Finalidad prevista

Practicar contratos de datos, evaluación de modelos, auditoría de subgrupos, documentación de gobernanza y apoyo a la revisión humana de casos simulados.

## 3. Usos no permitidos

- Perfilar territorios o poblaciones reales.
- Inferir riesgos reales a partir de estos datos sintéticos.
- Ejecutar intervenciones automáticas.
- Determinar elegibilidad de personas.
- Declarar emergencias o tomar decisiones reales únicamente a partir de una predicción.

## 4. Variables y grupos

El archivo contiene nueve columnas. La definición exacta de cada campo debe verificarse en el CSV y en el código de generación antes de interpretar sus valores.

La variable `protected_group` se reserva para auditoría de equidad y no debe utilizarse como predictor. `age_band` se trata como una dimensión sensible para el análisis de subgrupos, conforme a la configuración del proyecto.

No deben inferirse características de personas reales a partir de las etiquetas de los registros.

## 5. Calidad y limitaciones

Los patrones observados dependen de las reglas utilizadas para generar los datos. Por ello, los resultados de rendimiento y equidad sirven para probar el flujo técnico, pero no permiten estimar el desempeño sobre una población real.

Las métricas de intersecciones con muestras pequeñas presentan incertidumbre. Las diferencias entre grupos son señales para investigar, no pruebas de discriminación causal.

## 6. Privacidad, conservación y acceso

El conjunto está diseñado como sintético y no debe incorporar datos personales reales. Antes de cualquier sustitución por datos reales, será necesario evaluar finalidad, necesidad, minimización, acceso, seguridad, conservación y eliminación, conforme a las normas aplicables.

La política operativa de conservación y eliminación debe consultarse en `docs/DATA_INVENTORY_RETENTION.md`.

## 7. Uso en el sistema de apoyo a decisiones

El sistema es exclusivamente académico. Toda salida debe interpretarse con cautela y mantenerse bajo revisión humana. La existencia de una predicción no constituye autorización para actuar.

## 8. Trazabilidad

Consultar también:

- `docs/MODEL_CARD.md`
- `docs/RUNBOOK.md`
- `docs/RACI_HANDOFF.md`
- `docs/U04_E08_DECISION_RECORD.md`
- `reports/lab13/deployment_decision.json`
- `reports/lab13/INCIDENT_POSTMORTEM.md`
