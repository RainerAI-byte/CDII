# Inventario, minimización y retención de datos

**Asignatura:** INF-8239 Ciencia de Datos II  
**Unidad:** 04 — Ética y Roles en Ciencia de Datos  
**Ejercicio:** U04.E08 — Expediente de gobernanza y simulacro  
**Sistema:** Territorial Review DSS — Synthetic  
**Versión:** 1.0

## 1. Propósito y alcance

Este inventario documenta las categorías de datos utilizadas por el sistema experimental Territorial Review DSS — Synthetic, así como su finalidad, necesidad, acceso, medidas de protección y reglas propuestas de conservación.

El sistema utiliza datos sintéticos con fines exclusivamente académicos para practicar la evaluación de modelos, la auditoría de equidad y la gobernanza responsable. Los resultados no representan personas, territorios ni estadísticas oficiales de la República Dominicana.

El sistema no está autorizado para realizar intervenciones automáticas, determinar elegibilidad ni declarar emergencias.

## 2. Inventario de datos

| Categoría | Datos incluidos | Finalidad | Tratamiento |
|---|---|---|---|
| Variables predictoras | Variables numéricas y categóricas sintéticas | Alimentar el modelo experimental | Utilizar únicamente las variables necesarias para el objetivo académico |
| Variable objetivo | Etiqueta sintética de clasificación | Entrenar y evaluar el modelo | Separar correctamente entrenamiento y prueba |
| Variables de auditoría | `protected_group`, `age_band` | Evaluar diferencias de desempeño entre grupos | Utilizarlas para auditoría y análisis de limitaciones, no para justificar decisiones automáticas |
| Identificadores directos | Nombre, documento, correo y teléfono, cuando aparezcan en ejemplos o entradas | No son necesarios para el objetivo predictivo | Excluirlos del entrenamiento y de los reportes; no introducir identificadores reales |
| Métricas y resultados | Recall, precisión, FPR, diferencias entre grupos, tiempos y tamaño del modelo | Evaluación, reproducibilidad y gobernanza | Conservar los resultados necesarios para explicar y reproducir el experimento |
| Registros de gobernanza | Riesgos, responsables, decisiones, incidentes y acciones correctivas | Trazabilidad y supervisión | Registrar hechos verificables, responsables y fechas cuando estén disponibles |

La presencia de una categoría en este inventario no significa que todos sus campos existan en el dataset. El esquema efectivo debe verificarse contra los archivos y el código del proyecto.

## 3. Minimización de datos

Se aplicarán los siguientes controles:

1. Utilizar exclusivamente el dataset sintético previsto para el ejercicio.
2. No recopilar nombres, documentos de identidad, correos, teléfonos ni otros identificadores reales.
3. Excluir del entrenamiento cualquier identificador directo que pudiera incorporarse accidentalmente.
4. No añadir variables que no tengan una justificación documentada para el objetivo experimental.
5. Mantener las variables de auditoría separadas de la justificación de decisiones individuales.
6. Presentar métricas agregadas y explicar las limitaciones de los grupos con muestras pequeñas.
7. No publicar credenciales, archivos `.env` ni información personal en el repositorio.
8. Mantener los resultados de auditoría vinculados a la versión del dataset, el código y la configuración evaluada.

## 4. Acceso y responsabilidades

| Rol | Acceso y responsabilidad |
|---|---|
| Equipo de datos | Acceso técnico al dataset sintético, código, métricas y pruebas |
| Responsable institucional del ejercicio | Revisión del alcance, aprobación de controles y decisión sobre suspensión |
| Revisor humano | Interpretación de resultados, revisión de alertas y documentación de observaciones |
| Docente evaluador | Consulta de los artefactos académicos publicados y verificación de reproducibilidad |

Estos roles constituyen una propuesta para el ejercicio. No sustituyen una asignación formal de responsabilidades de la institución.

## 5. Política propuesta de retención

Como no se ha verificado una política institucional específica de conservación, los siguientes plazos son **propuestas operativas para el proyecto académico**, no obligaciones legales ni políticas oficiales de la UASD.

| Artefacto | Regla propuesta | Eliminación o revisión |
|---|---|---|
| Dataset sintético original | Conservar mientras sea necesario para reproducir el ejercicio | Revisar al cerrar la asignatura o cambiar la versión |
| Datos derivados y particiones | Conservar los necesarios para reproducir las métricas | Eliminar copias redundantes y temporales al finalizar la ejecución |
| Métricas y resultados de auditoría | Conservar como evidencia académica | Revisar si contienen información no necesaria |
| Logs temporales de ejecución | Conservar solo durante la depuración y validación | Eliminar cuando dejen de ser necesarios |
| Registros de decisiones e incidentes | Conservar junto con el expediente académico | Aplicar el plazo que determine la institución si existe una política formal |
| Modelos serializados | Conservar las versiones necesarias para reproducibilidad | Retirar versiones obsoletas cuando ya no sean necesarias |

La eliminación de archivos deberá considerar copias locales, carpetas temporales y versiones publicadas. La eliminación de un archivo del directorio de trabajo no garantiza que desaparezca de todo el historial de Git.

## 6. Controles de publicación

Antes de publicar el expediente en GitHub se debe comprobar que:

- Los datos publicados son sintéticos y compatibles con la finalidad académica.
- No existen credenciales, tokens, archivos `.env` ni identificadores personales reales.
- Las métricas pueden relacionarse con el código y la configuración que las generaron.
- Los reportes no contienen información innecesaria.
- Los documentos distinguen hechos observados, propuestas y decisiones humanas.
- Los cambios que afectan los resultados quedan registrados mediante control de versiones.

## 7. Limitaciones

Este inventario documenta el tratamiento previsto para el ejercicio académico. No constituye por sí solo una evaluación jurídica completa, una certificación de cumplimiento normativo ni una autorización para utilizar el sistema con datos reales.

Cualquier cambio hacia datos reales o uso operativo exige una nueva evaluación de finalidad, base jurídica, necesidad, proporcionalidad, seguridad, acceso, retención, equidad y supervisión humana.

## 8. Evidencia pendiente de verificación

Antes de considerar este artefacto definitivo, debe verificarse:

- El esquema real de columnas del dataset.
- Que los identificadores directos no se utilicen como variables predictoras.
- Que los archivos publicados no contengan información sensible o credenciales.
- Que los plazos propuestos se ajusten a cualquier política institucional aplicable, si existe.
