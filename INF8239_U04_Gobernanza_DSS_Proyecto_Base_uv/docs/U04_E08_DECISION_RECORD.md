# U04.E08 — Expediente de gobernanza

## Decisión humana

**Estado: REVIEW. Despliegue real no autorizado.**

El sistema se mantiene exclusivamente para evaluación académica con datos sintéticos. La salida automática GO de LAB13 no equivale a una autorización institucional.

## Evidencia revisada

- Dataset sintético: 640 observaciones y 9 columnas.
- Evaluación: 160 casos.
- Logistic Regression: exactitud 0.71875 y recall 0.71739.
- Logistic: diferencia de recall 0.13764 y diferencia de FPR 0.125.
- Tree: diferencia de recall 0.18130 y diferencia de FPR 0.16827.
- Límites configurados: recall mínimo 0.68, diferencia máxima de recall 0.16 y diferencia máxima de FPR 0.16.

Logistic cumple los dos límites de brechas agregadas configurados; tree no cumple ninguno. Esto no demuestra equidad integral ni justifica un uso real.

## Condiciones para reconsiderar la decisión

1. Investigar las intersecciones con recall inferior al 0.68.
2. Documentar la incertidumbre derivada de tamaños de muestra reducidos.
3. Verificar privacidad, calidad, finalidad y proporcionalidad antes de cualquier uso con datos reales.
4. Mantener revisión humana y prohibir decisiones automáticas.
5. Repetir auditorías y pruebas después de cada cambio del modelo o los datos.
6. Registrar evidencia, responsables, versión y aprobación formal antes de reconsiderar el estado.

## Usos prohibidos

- Intervención automática.
- Decisiones de elegibilidad.
- Declaraciones de emergencia.
- Decisiones reales sobre personas basadas únicamente en la predicción.

## Limitaciones

El conjunto de datos es sintético y no permite inferir el desempeño ni el impacto sobre poblaciones reales. Las diferencias entre grupos son señales para investigar, no pruebas causales de discriminación. No se ha medido directamente consumo eléctrico ni emisiones de carbono.

