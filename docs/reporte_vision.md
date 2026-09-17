# Reporte de Visión

## Descripción general

PatiTrack es un software diseñado para el Movimiento Estudiantil de Perritos y Gaticos de la Universidad de Antioquia. Su función es el registro y la gestión de las PQRS (Peticiones, Quejas, Reclamos y Sugerencias) relacionadas con la atención de perros y gatos, un proceso que actualmente se realiza de forma manual de voz a voz y a lápiz y papel.

## Problema que resuelve

PatiTrack recibe las PQRS por múltiples canales y las procesa manualmente, lo que genera:

- Riesgo de pérdida de información o de registros con datos errados.
- Falta de un número de radicado consecutivo y único, con riesgo de duplicados.
- Dificultad para archivar cada PQRS de forma independiente, con los datos propios de quien la interpone.
- Dificultad para garantizar una respuesta oportuna dentro del plazo estipulado (30 días calendario).

## Objetivos

- Digitalizar cada PQRS, evitando pérdidas o información errada.
- Registrar cada PQRS con un número de radicado consecutivo, evitando duplicados.
- Archivar cada PQRS de forma independiente, con la información de quién la interpone.
- Agilizar y garantizar la respuesta de cada PQRS almacenada dentro del tiempo estipulado, a través de los medios electrónicos suministrados por quien la interpone.

## Beneficios

- **Veracidad en la información:** al solicitar información personal, se asume la credibilidad de la persona, obteniendo datos y circunstancias propias del testigo o solicitante.
- **Organización:** al llevar un número de radicado único, se garantiza el almacenamiento de cada PQRS con sus propios datos.
- **Seguimiento:** cada PQRS obtiene un radicado que certifica los datos proporcionados y la fecha de creación, permitiendo un seguimiento que conlleva a la respuesta en el tiempo oportuno.
- **Efectividad:** evita que la información se pierda, al ser un programa que clasifica las solicitudes para PatiTrack.

## Alcance

Incluye el registro y consulta de PQRS, el cambio de estado (Registrada → En proceso → Solucionada), la impresión de radicados y la generación de cinco estadísticas (una obligatoria: promedio de días de respuesta). No incluye interfaz gráfica, base de datos relacional ni notificaciones automáticas a los solicitantes — el almacenamiento es mediante archivos planos, según lo definido por el docente.
