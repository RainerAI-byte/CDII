# \# Runbook — Territorial Review DSS - Synthetic

# 

# \## 1. Propósito y alcance

# 

# Este documento establece los procedimientos de supervisión, revisión humana, gestión de incidentes y suspensión del sistema Territorial Review DSS - Synthetic, desarrollado para el ejercicio académico INF-8239, Unidad 04.

# 

# El sistema utiliza datos sintéticos y se limita a la evaluación educativa de controles de gobernanza, equidad y Green AI. No está autorizado para tomar decisiones automáticas, intervenir sobre personas, determinar elegibilidad, declarar emergencias ni perfilar comunidades reales.

# 

# \## 2. Responsables

# 

# \- \*\*Responsable institucional designado:\*\* autoriza la continuidad del ejercicio, evalúa incidentes y puede ordenar la suspensión.

# \- \*\*Equipo de datos:\*\* ejecuta las evaluaciones, conserva los resultados, investiga brechas y documenta las limitaciones.

# \- \*\*Personal revisor:\*\* examina la evidencia disponible, documenta sus observaciones y evita depender exclusivamente de la puntuación del modelo.

# 

# \## 3. Supervisión y controles

# 

# Antes de considerar cualquier cambio de alcance, deben revisarse:

# 

# 1\. El desempeño global y las métricas por grupo e intersección.

# 2\. El recall mínimo configurado de 0.68.

# 3\. Las brechas máximas configuradas de recall y FPR, ambas de 0.16.

# 4\. La latencia máxima configurada de 500 ms.

# 5\. El tamaño máximo configurado del modelo de 1,024 KB.

# 6\. La integridad del conjunto sintético, la reproducibilidad y la trazabilidad de los resultados.

# 

# Los umbrales son controles definidos para este ejercicio y no constituyen, por sí solos, una certificación de seguridad o equidad.

# 

# \## 4. Estado de la evaluación actual

# 

# LAB13 produjo un resultado automático `GO` según las comprobaciones implementadas. Sin embargo, la auditoría interseccional de LAB12 registró:

# 

# \- G1, edades 30–44: recall de 0.5625.

# \- G1, edades 45–59: recall de aproximadamente 0.5882.

# 

# Ambos valores están por debajo del mínimo de 0.68. En consecuencia, la decisión humana documentada es `REVIEW` condicionado y no se autoriza el despliegue operativo.

# 

# El resultado automático original debe conservarse como evidencia; la decisión humana se registra por separado.

# 

# \## 5. Gestión de incidentes

# 

# Se consideran incidentes, entre otros:

# 

# \- Introducción de datos personales reales.

# \- Uso del sistema para una finalidad prohibida.

# \- Pérdida de trazabilidad o imposibilidad de reproducir los resultados.

# \- Incumplimiento de un control crítico.

# \- Uso de la salida como decisión automática.

# \- Exposición de información o acceso no autorizado.

# 

# \### Procedimiento

# 

# 1\. Registrar fecha, descripción, artefactos afectados y persona que reporta el incidente.

# 2\. Suspender el uso afectado cuando exista riesgo de incumplimiento o daño.

# 3\. Preservar los archivos, registros y resultados necesarios para investigar.

# 4\. Informar al responsable institucional designado.

# 5\. Determinar causa, alcance y controles correctivos.

# 6\. Documentar la decisión de mantener la suspensión o autorizar una reanudación controlada.

# 

# No debe afirmarse que un incidente fue resuelto hasta que exista evidencia verificable.

# 

# \## 6. Apelación y revisión humana

# 

# Toda observación o solicitud de revisión debe registrarse con:

# 

# \- Identificador del caso sintético.

# \- Motivo de la solicitud.

# \- Evidencia examinada.

# \- Persona responsable de la revisión.

# \- Resultado y justificación.

# \- Medidas correctivas, cuando correspondan.

# 

# El resultado del modelo es auxiliar y no sustituye el criterio humano. Este mecanismo es un procedimiento académico de revisión; no representa un canal institucional real habilitado para ciudadanos.

# 

# \## 7. Suspensión y rollback

# 

# Suspender el sistema si se detecta uso fuera del alcance autorizado, incorporación de datos reales, incumplimiento de controles críticos o imposibilidad de verificar los resultados.

# 

# Ante una suspensión:

# 

# 1\. Detener la ejecución o publicación de resultados afectados.

# 2\. Conservar una copia de la configuración y de la evidencia disponible.

# 3\. Identificar la última versión reproducible conocida.

# 4\. Documentar la causa y las medidas correctivas.

# 5\. Reanudar únicamente después de una revisión humana documentada y de comprobar los controles aplicables.

# 

# El rollback se refiere a volver a una versión controlada del código, configuración o artefactos. No elimina la necesidad de investigar el incidente.

# 

# \## 8. Registro de cambios y evidencias

# 

# Cada evaluación debe conservar, según corresponda:

# 

# \- Configuración de gobernanza.

# \- Identificación del dataset y del modelo.

# \- Métricas globales, por grupo e interseccionales.

# \- Registro de riesgos.

# \- Decisión automática original y decisión humana.

# \- Pruebas ejecutadas y resultados.

# \- Incidentes, apelaciones y acciones correctivas.

# \- Fecha, responsable y versión de los artefactos.

# 

# \## 9. Limitaciones

# 

# Los resultados disponibles proceden de un conjunto sintético y de una evaluación académica. No se han medido directamente el consumo eléctrico ni las emisiones de carbono. El tamaño del modelo y los tiempos registrados son indicadores operacionales parciales.

# 

# La evaluación actual no demuestra que el sistema sea apto para despliegue operativo ni que esté libre de sesgo.

# 

# \## 10. Decisión vigente

# 

# \*\*Estado humano: REVIEW condicionado.\*\*

# 

# Se permite continuar con el trabajo académico y la documentación utilizando datos sintéticos. No se autoriza el despliegue operativo. Cualquier reconsideración requiere investigar las brechas interseccionales, documentar las medidas correctivas y revisar la evidencia antes de tomar una nueva decisión.

