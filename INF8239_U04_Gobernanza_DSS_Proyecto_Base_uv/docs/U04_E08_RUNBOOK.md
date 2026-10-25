# U04.E08 — Runbook operativo

## Estado actual
Sistema académico con datos sintéticos. No autorizado para producción ni para decisiones reales sobre personas.

## 1. Detección
Activar revisión ante incumplimiento de los gates configurados, caída del recall, aumento de brechas entre grupos, datos inválidos, cambios no aprobados o comportamiento inesperado de la aplicación.

## 2. Contención
Detener el uso de la salida para orientar acciones. Cambiar el estado operativo a REVIEW/STOP según la gravedad. Mantener el sistema fuera de decisiones automatizadas y volver al procedimiento manual seguro.

## 3. Preservación de evidencia
Guardar fecha y hora, versión del código, versión/configuración del modelo, archivos de métricas, registros de ejecución y descripción del incidente. No modificar los archivos originales de evidencia.

## 4. Comunicación
Notificar al responsable institucional y al responsable técnico. Incluir alcance, impacto conocido, incertidumbres, acciones de contención y decisión temporal. No declarar daños o causas que no se hayan verificado.

## 5. Reversión
Deshabilitar la versión afectada y volver al proceso manual o a una versión previamente validada. Verificar que no se ejecuten decisiones automáticas. Registrar quién autorizó la reversión y cuándo.

## 6. Corrección y recuperación
Analizar la causa, definir responsable y fecha para cada acción correctiva, ejecutar pruebas de regresión y repetir la auditoría por grupo e intersección. No levantar la restricción hasta contar con evidencia revisada y aprobación humana formal.

## 7. Cierre
El postmortem debe registrar detección, contención, evidencia preservada, comunicación, reversión, acciones correctivas, responsables, fechas y criterios de cierre.
