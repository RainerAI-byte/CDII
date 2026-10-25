# Matriz RACI y traspaso entre roles

**Asignatura:** INF-8239 Ciencia de Datos II  
**Unidad:** 04 — Ética y Roles en Ciencia de Datos  
**Ejercicio:** U04.E08 — Expediente de gobernanza y simulacro  
**Sistema:** Territorial Review DSS — Synthetic

## 1. Objetivo

Establecer responsabilidades para la preparación de datos, evaluación del modelo, auditoría de equidad, revisión de riesgos, gestión de incidentes y decisión final sobre el uso del sistema.

La matriz es una propuesta de gobernanza académica. No representa una asignación oficial de cargos o responsabilidades dentro de la UASD.

## 2. Definición de roles

- **ET — Equipo técnico de datos:** prepara los datos, ejecuta el código, verifica las pruebas y documenta las métricas.
- **RI — Responsable institucional del ejercicio:** responde por la decisión final sobre el alcance autorizado y puede ordenar la suspensión del ejercicio.
- **RH — Revisor humano:** interpreta las salidas, revisa alertas y documenta observaciones sin delegar su criterio al modelo.
- **DP — Docente o supervisor académico:** verifica que el trabajo cumpla los objetivos de la asignatura y que las conclusiones tengan evidencia.

En la matriz, **R** significa responsable de ejecutar; **A**, responsable último de aprobar o responder por la actividad; **C**, consultado; e **I**, informado. Cada actividad debe tener una única asignación A.

## 3. Matriz RACI

| Actividad | ET | RI | RH | DP |
|---|---|---|---|---|
| Documentar el dataset y su finalidad | R | A | C | I |
| Preparar y validar los datos | R | A | C | I |
| Entrenar y evaluar el modelo | R | A | C | I |
| Ejecutar auditorías por grupo e intersección | R | A | C | I |
| Documentar riesgos y limitaciones | R | A | C | I |
| Aprobar el alcance académico de uso | C | A/R | C | I |
| Revisar resultados antes de cualquier uso | C | A | R | I |
| Registrar una queja o posible incidente | C | A | R | I |
| Investigar técnicamente un incidente | R | A | C | I |
| Suspender el uso si fallan los controles | C | A/R | C | I |
| Documentar acciones correctivas | R | A | C | I |
| Verificar la entrega académica | C | I | I | A/R |

La asignación A/R indica que, para esa actividad, el rol tiene tanto la responsabilidad de ejecución como la responsabilidad última. La matriz deberá ajustarse si se incorporan roles reales o procedimientos institucionales.

## 4. Protocolo de traspaso entre roles

### Etapa 1. Equipo técnico → Responsable institucional

El equipo técnico entrega:

- Versión del dataset y su ficha descriptiva.
- Código y configuración utilizados.
- Métricas globales y por grupo.
- Diferencias interseccionales identificadas.
- Registro de riesgos y limitaciones.
- Resultado de pruebas y recursos computacionales.

El responsable institucional verifica que los resultados sean trazables y que el alcance propuesto respete las restricciones definidas.

### Etapa 2. Responsable institucional → Revisor humano

El responsable entrega una instrucción de revisión que indique:

- Finalidad y límites del sistema.
- Métricas y umbrales configurados.
- Grupos que requieren atención.
- Limitaciones conocidas.
- Criterios para documentar una observación y solicitar una nueva revisión.

El revisor humano no debe tratar la predicción como una decisión definitiva ni asumir que superar las métricas globales elimina los riesgos de los subgrupos.

### Etapa 3. Revisor humano → Responsable institucional

El revisor registra:

- Resultado de la revisión.
- Evidencia examinada.
- Incertidumbres y limitaciones.
- Desviaciones observadas.
- Recomendación: continuar dentro del alcance académico, modificar, limitar o suspender.
- Necesidad de nueva evaluación o de acciones correctivas.

El responsable institucional documenta la decisión y sus fundamentos.

### Etapa 4. Responsable institucional → Equipo técnico

La decisión debe indicar las modificaciones requeridas, el responsable de cada acción y la evidencia necesaria para cerrar la observación.

El equipo técnico implementa los cambios, ejecuta las pruebas correspondientes y entrega los nuevos resultados. La modificación del código no sustituye la aprobación humana.

## 5. Aplicación a los resultados de LAB12 y LAB13

En el experimento se observó que el recall global fue aproximadamente 71.74 %, mientras que algunos grupos interseccionales presentaron resultados inferiores al umbral configurado de 68 %.

Por ello, el traspaso debe comunicar que el resultado automático de los controles fue `GO`, pero la revisión humana final permanece en `REVIEW`, sin autorización para despliegue operativo.

Las acciones requeridas son investigar las diferencias, documentar limitaciones, mantener supervisión humana y conservar el uso restringido a datos sintéticos y fines académicos.

## 6. Evidencia de trazabilidad

El expediente debe conservar, cuando estén disponibles:

- Identificador y fecha de la versión evaluada.
- Responsable de cada revisión.
- Evidencia recibida y entregada.
- Observaciones y decisiones.
- Acciones correctivas y su estado.
- Referencia al commit o versión de código relacionada.

No se deben inventar firmas, fechas, aprobaciones ni responsables institucionales reales. Si una actividad todavía no se ha ejecutado, debe registrarse como pendiente.

## 7. Limitaciones

Esta matriz define un modelo de responsabilidades para el ejercicio académico. No sustituye las funciones oficiales de la institución ni constituye por sí sola un procedimiento administrativo aprobado.
