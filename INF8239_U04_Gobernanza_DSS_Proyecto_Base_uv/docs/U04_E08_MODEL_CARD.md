# U04.E08 — Model Card

## Identificación
Sistema: Territorial Review DSS - Synthetic.
Modelo de referencia: Logistic Regression.
Uso previsto: priorizar casos sintéticos para revisión humana en un ejercicio académico.
Estado: REVIEW; despliegue real no autorizado.

## Datos y evaluación
Dataset sintético de 640 filas y 9 columnas. La evaluación reportada utiliza 160 casos. La partición y el procedimiento se describen en el código del proyecto y los reportes de LAB12.

## Resultados observados
Logistic: accuracy 0.71875; recall 0.71739; precision 0.77647; FPR 0.27941; diferencia de recall 0.13764; diferencia de FPR 0.125; entrenamiento 0.04797 s; tamaño serializado 3.5635 KB.

Tree: accuracy 0.70625; recall 0.71739; precision 0.75862; FPR 0.30882; diferencia de recall 0.18130; diferencia de FPR 0.16827; entrenamiento 0.06020 s; tamaño serializado 7.8701 KB.

## Límites y riesgos
Los resultados dependen del dataset sintético, la partición y la configuración. Las métricas agregadas pueden ocultar errores en intersecciones. Algunos subgrupos tienen pocas observaciones. No se demuestra causalidad ni se garantiza generalización.

## Uso no permitido
No usar para decisiones reales de elegibilidad, intervención, emergencia ni para automatizar decisiones sobre personas. No interpretar la salida como verdad definitiva.

## Supervisión humana
Toda predicción requiere revisión humana. La decisión automática GO de los controles técnicos no sustituye la autorización institucional. El estado humano documentado es REVIEW.

## Monitoreo y revisión
Antes de cualquier reconsideración: revisar recall y FPR por grupo e intersección, verificar calidad de datos, registrar incidentes, revisar cambios de distribución y conservar versiones del modelo, configuración y evidencia.
