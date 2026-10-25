# Simulacro de incidente — U04.E08

- detected_at_utc: 2026-10-25T13:50:03.035715+00:00
- scenario: incumplimiento de umbral de equidad detectado durante revisión de resultados
- signal: el modelo Tree presenta recall_gap=0.18130 y fpr_gap=0.16827, superiores a los límites 0.16 configurados
- containment: estado REVIEW; no autorizar despliegue ni decisiones automáticas; mantener revisión humana
- evidence_preserved: reports/lab12/tree/global_metrics.json, fairness_by_group.csv, fairness_intersectional.csv; conservar configuración y versión del código
- communication: informar al responsable técnico y al responsable institucional; explicar métricas, alcance, incertidumbre y restricciones
- rollback: mantener el sistema fuera de producción y usar revisión manual; no desplegar la versión que incumple gates
- corrective_actions:
  1. Owner: responsable de datos; due_date: por asignar; action: investigar calidad de datos y composición de grupos
  2. Owner: responsable de modelado; due_date: por asignar; action: analizar errores por grupo e intersección y evaluar alternativas
  3. Owner: responsable institucional; due_date: por asignar; action: revisar la decisión y autorizar formalmente cualquier cambio de estado
- recovery_criteria: repetir pruebas y auditoría; documentar resultados y revisión humana antes de reconsiderar el estado
- limitations: simulacro académico con datos sintéticos; no representa un incidente real ni demuestra impacto sobre personas


