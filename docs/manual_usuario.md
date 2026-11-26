# Manual de usuario — PatiTrack

## Requisitos y ejecución

Esta guía explica cómo preparar un equipo Windows, abrir el proyecto y ejecutar
PatiTrack. No es necesario que la carpeta tenga un nombre específico.

### 1. Instalar Python o Anaconda

PatiTrack está escrito en Python y utiliza módulos incluidos con Python; no
requiere instalar paquetes adicionales con pip.

Elija una de estas alternativas:

- **Python directamente:** descargue Python 3 desde
  [python.org](https://www.python.org/downloads/windows/). Para este proyecto
  puede usar Python 3.12, que ya se utilizó durante el desarrollo.
- **Anaconda:** descárguelo desde
  [anaconda.com](https://www.anaconda.com/download). Anaconda incluye Python y
  herramientas como Jupyter. No hace falta instalar también Python por
  separado.

Durante la instalación, siga las indicaciones del instalador oficial. Si la
computadora pertenece a la universidad, puede que se necesite autorización para
instalar programas; en ese caso, consulte al administrador del equipo.

Para comprobar la instalación, abra PowerShell o Anaconda Prompt y escriba:

    python --version

Debe aparecer una versión de Python 3. Si Windows indica que no reconoce
python, abra Anaconda Prompt si eligió Anaconda, o revise la instalación de
Python y vuelva a abrir la terminal.

### 2. Instalar Visual Studio Code

Descargue [Visual Studio Code](https://code.visualstudio.com/download) e
instálelo con las opciones recomendadas. En Visual, abra la vista de
extensiones con **Ctrl+Shift+X**, busque la extensión **Python** publicada por
Microsoft e instálela. Visual Studio Code es el editor; la extensión agrega
funciones para Python, pero no reemplaza al intérprete que instaló en el paso
anterior. La guía oficial de VS Code explica también cómo elegir un intérprete:
[Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial).

### 3. Elegir el intérprete en Visual Studio Code

1. Abra la paleta de comandos con **Ctrl+Shift+P**.
2. Escriba **Python: Select Interpreter** y selecciónelo.
3. Elija el Python 3 instalado o el entorno de Anaconda que usará.
4. Abra **Terminal > New Terminal** y escriba python --version para confirmar
   que la terminal reconoce el mismo intérprete.

Si se cambia de intérprete, cierre las terminales abiertas y cree una nueva
para que se active la selección.

### 4. Abrir la carpeta correcta del proyecto

Descargue el proyecto desde GitHub o use la copia recibida del equipo. Si lo
descarga como ZIP, extráigalo primero. En Visual Studio Code, seleccione
**File > Open Folder** y abra la carpeta raíz que contiene **src/**, **docs/**,
**data/** y **run.bat**. No abra únicamente **src/**: el menú se ejecuta como
parte del paquete src.

La ubicación y el nombre de la carpeta pueden ser distintos en cada equipo.
PatiTrack guarda sus archivos dentro de la carpeta **data/** del proyecto.

### 5. Ejecutar PatiTrack

**Opción A — doble clic en Windows:** haga doble clic en **run.bat**, ubicado
en la carpeta raíz. El archivo cambia automáticamente a la carpeta del
proyecto y ejecuta el menú. Esta opción necesita que Windows encuentre el
comando python.

**Opción B — terminal de Visual Studio Code:** abra **Terminal > New
Terminal**, confirme que la ruta mostrada corresponde a la carpeta raíz del
proyecto y ejecute:

    python -m src.main

Si usa Anaconda y el comando anterior no reconoce el entorno seleccionado,
ejecútelo desde Anaconda Prompt, después de ubicarse en la carpeta raíz.

### Solución de problemas de inicio

- **No module named src:** la terminal está en otra carpeta. Abra en Visual
  Studio Code la raíz del proyecto y vuelva a ejecutar el comando.
- **python no se reconoce:** seleccione el intérprete correcto, abra una
  terminal nueva o use Anaconda Prompt si instaló Anaconda.
- **run.bat no encuentra Python:** ejecute el comando desde Visual Studio Code
  con el intérprete seleccionado o desde Anaconda Prompt.
- **El repositorio ya existe al ejecutar git clone:** no repita la clonación.
  Entre a la carpeta descargada y actualícela con git pull origin main.
- **Aparece un error de sintaxis en un archivo:** confirme que está usando una
  copia actualizada del repositorio y no una copia anterior guardada en otra
  carpeta.

Para probar el programa, use información ficticia. Los registros se guardan
como texto en **data/**; evite subir al repositorio datos personales reales.

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
