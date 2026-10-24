# Model Card — Territorial Review DSS

## 1. Identificación
- Sistema: Territorial Review DSS - Synthetic
- Modelo evaluado: Logistic Regression
- Proyecto: INF-8239, Unidad 04
- Finalidad: ejercicio educativo de gobernanza, equidad y Green AI.

## 2. Uso previsto
Priorizar casos sintéticos para revisión humana. La predicción constituye una señal auxiliar y no una decisión definitiva.

## 3. Usos prohibidos
- Intervención automática.
- Decisiones de elegibilidad.
- Declaraciones de emergencia.
- Perfilamiento de personas o comunidades reales.
- Uso operativo con datos personales reales.

## 4. Datos
El conjunto de datos es sintético y educativo. No representa personas, territorios, tasas ni estadísticas oficiales de República Dominicana.

## 5. Resultados globales
- Casos evaluados: 160.
- Accuracy: 71.88 %.
- Recall: 71.74 %.
- Brecha de recall entre grupos: 13.76 puntos porcentuales.
- Brecha de FPR entre grupos: 12.50 puntos porcentuales.
- Tiempo de entrenamiento reportado por LAB12: 0.048 segundos.
- Tamaño del modelo: 3.56 KB.

## 6. Equidad e intersecciones
El recall observado fue:
- G1, edades 30–44: 56.25 % (24 casos).
- G1, edades 45–59: 58.82 % (35 casos).

Ambos segmentos están por debajo del recall mínimo configurado de 68 %. Los resultados de segmentos pequeños deben interpretarse con cautela y no constituyen evidencia sobre poblaciones reales.

## 7. Limitaciones
- Los resultados dependen del conjunto sintético y del protocolo experimental.
- Las métricas agregadas pueden ocultar diferencias entre subgrupos.
- La auditoría no demuestra ausencia de sesgo ni garantiza seguridad operativa.
- El tiempo de entrenamiento no equivale al consumo energético total.
- No se han presentado mediciones directas de electricidad o emisiones de carbono.

## 8. Decisión y restricciones
El control automático de LAB13 produjo el estado GO según sus cinco comprobaciones configuradas. Sin embargo, la revisión humana queda en REVIEW condicionado porque dos intersecciones presentan recall inferior al mínimo.

No se autoriza el despliegue operativo. El uso permanece limitado a fines educativos y datos sintéticos.

## 9. Requisitos antes de reconsiderar la decisión
- Investigar las diferencias interseccionales.
- Documentar controles correctivos y nueva evidencia.
- Mantener revisión humana, trazabilidad y mecanismo de apelación.
- Verificar los controles antes de reconsiderar cualquier cambio de alcance.

## 10. Responsabilidad
El responsable institucional designado puede restringir o suspender el sistema. El equipo de datos debe documentar evaluaciones, limitaciones, incidentes y medidas correctivas.