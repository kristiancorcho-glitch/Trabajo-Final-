# Especificación de Requisitos

## Resumen ejecutivo

El software es un sistema de gestión para el registro, validación y seguimiento de Peticiones, Quejas, Reclamaciones y Sugerencias (PQRS) de la Facultad de Ingeniería. El sistema procesa los datos mediante cuatro archivos planos independientes (`Peticion.txt`, `Queja.txt`, `Reclamo.txt` y `Sugerencia.txt`), asignando secuencias de registro autoincreméntales e independientes para cada archivo.

## Requisitos funcionales

Los requisitos funcionales detallan el comportamiento del software y las operaciones que debe ejecutar para garantizar la integridad de los datos en la captura, validación y gestión de las solicitudes.

- **RF-01: Registro y autoincremento de ID por archivo**
  - El sistema debe asignar automáticamente a cada nuevo registro un identificador entero autoincremental que inicie en 1.
  - La secuencia de ID debe ser independiente para cada uno de los cuatro archivos planos de almacenamiento.

- **RF-02: Validación estricta de datos del solicitante**
  - **Nombre completo:** obligatorio, entre 3 y 100 caracteres, permite solo letras, espacios, tildes, apóstrofes (') y guiones (-). Rechaza números y otros caracteres especiales.
  - **Tipo de documento:** obligatorio, solo permite los valores CC, TI, CE, PP y NIT.
  - **Número de documento:** obligatorio, numérico, de 3 a 15 dígitos. Rechaza letras y caracteres especiales.
  - **Teléfono:** exige seleccionar el tipo de teléfono (Celular, Fijo, Corporativo, Otro) y valida que el teléfono de contacto tenga exactamente 10 dígitos numéricos.
  - **Correo electrónico:** obligatorio, valida estructura sintácticamente correcta (`correo@dominio.com`), un único símbolo `@` y longitud máxima de 254 caracteres.
  - **Dirección:** opcional, de 5 a 200 caracteres, permite caracteres habituales de nomenclatura (#, -, ., /).

- **RF-03: Validación de información de la PQRS y datos relacionados**
  - **Tipo de solicitud:** selección obligatoria entre Petición, Queja, Reclamo o Sugerencia, la cual determina el archivo plano de destino.
  - **Fecha de radicación:** se registra en formato `datetime` de Python, bloqueando fechas futuras.
  - **Canal de recepción:** selección obligatoria entre Presencial, Correo electrónico, Página web, Teléfono, Redes sociales u Otro.
  - **Asunto y descripción:** asunto de 5 a 150 caracteres; descripción detallada obligatoria de 20 a 2.000 caracteres (debe contener texto real, no solo espacios).
  - **Mascota y campus:** selección obligatoria del tipo de mascota (Perro o Gato) y del campus relacionado, entre los 9 predios autorizados de la universidad.

- **RF-04: Gestión automática de tiempos y flujo de estado**
  - **Fecha máxima de respuesta:** se calcula automáticamente sumando exactamente 30 días calendario a la fecha de radicación, usando `datetime`.
  - **Control de estado:** todo registro se inicializa obligatoriamente en estado *Registrada*. El sistema debe forzar que las transiciones sigan exclusivamente el flujo secuencial: Registrada → En proceso → Solucionada.

## Requisitos no funcionales

Los requisitos no funcionales establecen los criterios de calidad, arquitectura, rendimiento y usabilidad que rigen la operación del software.

- **RNF-01: Usabilidad e interacción visual**
  - La interfaz debe ofrecer retroalimentación en tiempo real durante la entrada de datos, resaltando errores de formato antes del envío e inhabilitando la radicación si existen campos no válidos.

- **RNF-02: Arquitectura del software y almacenamiento**
  - El sistema debe construirse mediante Programación Orientada a Objetos (POO), implementando clases con el prefijo `c_` (`c_Peticion`, `c_Queja`, `c_Reclamo`, `c_Sugerencia`) y utilizando comprensión de listas para la manipulación y filtrado de datos.
  - La persistencia debe realizarse exclusivamente en cuatro archivos de texto plano independientes, manteniendo una estructura de datos homogénea.

- **RNF-03: Rendimiento y eficiencia**
  - El procesamiento de las validaciones de texto, los cálculos de fechas (`datetime`) y la inserción en los archivos planos deben ejecutarse de forma inmediata, manteniendo respuestas visuales menores a 200 milisegundos.

- **RNF-04: Fiabilidad e integridad de datos**
  - El sistema debe garantizar que la escritura en los archivos `.txt` no corrompa la secuencia de los ID ni permita registros duplicados o incompletos ante fallos de captura.
