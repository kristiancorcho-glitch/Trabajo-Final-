# Plan de Versionado

**Proyecto:** PatiTrack — Gestor de PQRS  
**Curso:** Algoritmia y Programación — Proyecto Integrador 2026-2

## Objetivo

Registrar los hitos del proyecto desde su inicio hasta la entrega final, indicando los cambios previstos o realizados en cada versión, sus responsables y su fecha. Este plan reúne el historial de trabajo del equipo y la descripción funcional de las versiones.

## Referencia temporal

- **Día 0:** 2 de septiembre de 2026, fecha de la reunión inicial del equipo (Acta #1).
- Los días indicados son días calendario transcurridos desde el Día 0.
- **Día 16:** 18 de septiembre de 2026, Entrega 1 (puntos 1 a 7).
- **Día 86:** 27 de noviembre de 2026, entrega final del proyecto.
- **Sustentaciones:** 2 y 4 de diciembre de 2026.

## Esquema de versionado

Se utiliza el formato `vMAJOR.MINOR.PATCH`:

| Componente | Significado |
| --- | --- |
| MAJOR | Permanece en 0 mientras el programa no esté completo. Cambia a 1 con la primera versión final funcional. |
| MINOR | Aumenta al completar un hito relevante del proyecto, como un documento clave, módulo o entrega. |
| PATCH | Aumenta para correcciones menores que no agregan funcionalidades. |

Al completar y revisar una versión, se registrará con un tag en GitHub. Danny Milena García Gonzales es responsable de mantener el historial de versiones. Las versiones futuras y sus fechas son objetivos de trabajo; se actualizarán si cambia el cronograma o el alcance.

## Trabajo en GitHub

- La rama `main` contiene la versión estable más reciente.
- Los integrantes desarrollan sus cambios en ramas de trabajo (por ejemplo, `feature/validaciones`) y los incorporan a `main` mediante pull request con revisión de otro integrante.
- Cada persona sube los avances desde su propia cuenta para que su participación quede registrada en el historial.
- Los mensajes de commit usan el formato `tipo: descripción breve`, por ejemplo: `feat: agrega validación de correo`, `fix: corrige consecutivo de Queja.txt` y `docs: actualiza README`.

## Historial y plan de versiones

| Versión | Día y fecha | Hito y alcance | Responsable(s) | Avance acumulado estimado | Estado |
| --- | --- | --- | --- | ---: | --- |
| v0.1.0 | Día 0 · 02/09/2026 | **Inicio y organización.** Reunión inicial, creación de usuarios de GitHub, socialización del repositorio y asignación de roles (Acta #1). Organización inicial del repositorio y definición de las actas del equipo; inicio del README, la identidad PatiTrack y la estructura prevista para código, documentos, imágenes y datos. | Todo el equipo | 5 % | Realizada |
| v0.2.0 | Día 15 · 17/09/2026 | **Análisis y revisión de la Entrega 1.** Revisión conjunta de los puntos 1 a 7 y ajustes previos a la entrega (Acta #2). Consolidación de la visión, los requisitos y el plan de proyecto; revisión de la arquitectura modular y los campos que almacenará cada tipo de PQRS. | Todo el equipo | 15 % | Realizada |
| v0.3.0 | Día 16 · 18/09/2026 | **Entrega 1: documentación inicial.** README con integrantes, vínculos académicos, nombre y detalles del proyecto, licencia, reporte de visión, especificación de requisitos y plan de proyecto. Esta entrega corresponde a los puntos 1 a 7. | Todo el equipo | 20 % | Realizada |
| v0.4.0 | Día 27 · 29/09/2026 | **Planificación del desarrollo.** Elaboración del plan de versionado y creación del Colab de trabajo (Acta #3). | Kristian, Danny y Carlos | 25 % | Realizada |
| v0.5.0 | Día 42 · 14/10/2026 | **Ajustes de documentación y colaboración.** Completar los datos académicos pendientes del README, actualizar las actas de entendimiento, colaboración y responsabilidad con las firmas correspondientes, y mantener los aportes del equipo en GitHub. | Todo el equipo | 30 % | Planificada |
| v0.6.0 | Día 49 · 21/10/2026 | **Diseño del programa.** Definir las clases `c_Peticion`, `c_Queja`, `c_Reclamo` y `c_Sugerencia`, la estructura de datos compartida —incluido `fecha_solucion`— y el menú de consola para registrar, consultar, cambiar estados, ver estadísticas y salir. | Kristian, Danny y Danilo | 40 % | Realizada |
| v0.7.0 | Día 56 · 28/10/2026 | **Validaciones.** Crear `validaciones.py` para validar nombres, documentos, teléfonos, correos, direcciones, fechas y opciones seleccionadas; incluir mensajes que permitan corregir los datos inválidos. | Kristian y Danny | 50 % | Planificada |
| v0.8.0 | Día 63 · 04/11/2026 | **Registro y almacenamiento.** Implementar el registro de PQRS y `archivos.py` para leer y escribir los cuatro archivos planos (`Peticion.txt`, `Queja.txt`, `Reclamo.txt` y `Sugerencia.txt`). Asignar un ID consecutivo independiente por archivo y calcular la fecha máxima de respuesta a 30 días calendario de la radicación. Incluir el campo `fecha_solucion`, inicialmente vacío. | Todo el equipo | 62 % | Planificada |
| v0.9.0 | Día 70 · 11/11/2026 | **Consulta, estados y radicados.** Consultar las PQRS y su estado, permitir las transiciones Registrada → En proceso → Solucionada y guardar automáticamente `fecha_solucion` al completar la última transición. Imprimir el comprobante ASCII de 120 caracteres, con la información requerida y dirección opcional como `N/A`. | Todo el equipo | 75 % | Planificada |
| v0.10.0 | Día 75 · 16/11/2026 | **Estadísticas.** Crear `reportes.py` con el promedio de días transcurridos entre `fecha_radicacion` y `fecha_solucion` para las PQRS solucionadas, más cinco estadísticas adicionales. Como propuestas iniciales: cantidades por tipo de solicitud, cantidades por tipo de mascota, PQRS más antigua, próximas a vencer y distribución por campus. | Todo el equipo | 85 % | Planificada |
| v0.11.0 | Día 80 · 21/11/2026 | **Integración y verificación.** Integrar los módulos y comprobar el flujo de registro, validaciones, almacenamiento, consulta, estados, radicados y reportes frente a los requisitos del proyecto. | Todo el equipo | 92 % | Planificada |
| v0.12.0 | Día 83 · 24/11/2026 | **Correcciones y manual.** Resolver los errores encontrados, completar el manual de usuario en `docs/` y revisar que el repositorio contenga el código, documentación, imágenes y archivos de datos en las carpetas establecidas. | Carlos y todo el equipo | 97 % | Planificada |
| v1.0.0 | Día 86 · 27/11/2026 | **Entrega final.** Publicar la versión funcional del proyecto con el código en `src/`, documentación y manual en `docs/`, elementos gráficos en `images/` y archivos planos en `data/`. Preparar el programa para la sustentación. | Todo el equipo | 100 % | Planificada |

## Seguimiento

- “Realizada” identifica un hito que el equipo ya completó; “Planificada” indica una meta futura y no afirma que el trabajo esté terminado.
- Los porcentajes son estimaciones de avance acumulado del equipo, no resultados de una medición automática. Se actualizan al revisar cada hito.
- Si cambian las fechas del curso o las prioridades del equipo, se registra el ajuste en el siguiente seguimiento o acta.
- Las correcciones posteriores a la entrega final se identifican como `v1.0.1` y siguientes, de acuerdo con el cambio realizado.

## Regla para calcular el promedio de respuesta

Al cambiar una PQRS a *Solucionada*, el programa guarda automáticamente la fecha actual en `fecha_solucion`. El promedio se calcula como la diferencia en días calendario entre `fecha_radicacion` y `fecha_solucion`, considerando únicamente las PQRS solucionadas. Si todavía no hay registros solucionados, el programa informa que no hay datos suficientes. Las cinco estadísticas adicionales propuestas se validarán con el docente y con las necesidades del gestor.
