# Manual de usuario — PatiTrack

## Requisitos y ejecución

### Preparar el equipo

Antes de ejecutar PatiTrack:

1. Instale Python 3 directamente o instale Anaconda, que incluye Python.
   No es necesario instalar ambos.
2. Instale Visual Studio Code (Visual) como editor de código.
3. Si usa Visual Studio Code, instale o habilite la extensión oficial de
   Python y seleccione el intérprete de Python instalado.

### Iniciar el programa

Con Python disponible, abra una terminal en la carpeta raíz del proyecto y
ejecute:

```powershell
python -m src.main
```

En Windows también puede iniciar PatiTrack haciendo doble clic en `run.bat`,
ubicado en la carpeta raíz del proyecto. El iniciador cambia automáticamente
a esa carpeta, así que el proyecto puede estar dentro de otra ruta o tener otro
nombre.

El programa funciona en consola y presenta un menú con cinco opciones.

## Ejecución opcional en Google Colab

Esta opción requiere que la versión actualizada del proyecto esté disponible
en GitHub. En un cuaderno nuevo de Colab, ejecute estas instrucciones en dos
celdas separadas:

```python
!git clone https://github.com/kristiancorcho-glitch/Trabajo-Final-.git
%cd /content/Trabajo-Final-
```

La celda de clonación se ejecuta una sola vez por entorno. Si la carpeta ya
existe, no vuelva a clonarla: actualice la copia con:

```python
%cd /content/Trabajo-Final-
!git pull origin main
```

Después puede ejecutar la celda del menú:

```python
from src.main import ejecutar_menu

ejecutar_menu()
```

Las respuestas a las preguntas del menú se ingresan en la salida de la segunda
celda. Los archivos de datos quedan en el entorno temporal de Colab y pueden
perderse cuando este se reinicie o se elimine. Descargue los archivos que
necesite conservar antes de cerrar la sesión. Para demostraciones, use datos
ficticios en lugar de información personal.

## Registrar una PQRS

1. Seleccione **1. Registrar PQRS**.
2. Ingrese los datos del solicitante. La dirección es opcional; presione Enter
   para omitirla.
3. Seleccione el tipo de solicitud, ingrese la fecha de radicación y complete
   canal, asunto, descripción, tipo de mascota y campus.
4. Si un dato no cumple las reglas, el programa muestra el error y vuelve a
   solicitarlo.
5. Al finalizar, el programa guarda la solicitud, asigna el ID consecutivo de
   su tipo y muestra un comprobante.

La fecha máxima de respuesta se calcula sumando 30 días calendario a la fecha
de radicación. Cada tipo mantiene su propio consecutivo, que comienza en 1.

## Consultar una PQRS

1. Seleccione **2. Consultar PQRS**.
2. Elija el tipo de solicitud.
3. Ingrese el ID que aparece en el comprobante.
4. Revise los datos y, si lo desea, solicite que se muestre nuevamente el
   comprobante.

## Cambiar el estado

1. Seleccione **3. Cambiar estado de una PQRS**.
2. Elija el tipo e ingrese el ID.
3. Confirme el siguiente estado cuando el programa lo solicite.

El flujo permitido es **Registrada → En proceso → Solucionada**. Al pasar a
Solucionada, el programa guarda la fecha del día. Una solicitud solucionada no
puede avanzar a otro estado.

## Ver estadísticas

Seleccione **4. Ver estadísticas** para consultar:

- Promedio de días entre radicación y solución.
- Cantidad de PQRS por tipo de solicitud.
- Cantidad por tipo de mascota.
- PQRS pendiente más antigua.
- PQRS que vencen hoy o en los próximos cinco días.
- Cantidad por campus.

Si todavía no hay solicitudes solucionadas, el promedio se informa como no
disponible.

## Archivos de datos

El programa crea la carpeta data si no existe y guarda los registros en cuatro
archivos de texto UTF-8: Peticion.txt, Queja.txt, Reclamo.txt y Sugerencia.txt.
Los campos se separan con punto y coma; los valores que contengan separadores
o saltos de línea se guardan entrecomillados para conservarse al volver a
leerlos. No edite los archivos mientras el programa está funcionando.

Cada registro contiene el ID y los campos acordados: datos del solicitante,
tipo de PQRS, fechas, canal, asunto, descripción, mascota, campus, estado y
fecha de solución.

## Salir

Seleccione **5. Salir** para cerrar el programa.
