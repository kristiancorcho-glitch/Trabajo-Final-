"""Persistencia de las PQRS en cuatro archivos de texto delimitados por punto y coma."""

import csv
import os
import tempfile
import unicodedata
from datetime import date, datetime
from pathlib import Path

CARPETA_DATA = Path(__file__).resolve().parent.parent / "data"
ARCHIVOS_POR_TIPO = {
    "peticion": ("Petición", "Peticion.txt"),
    "queja": ("Queja", "Queja.txt"),
    "reclamo": ("Reclamo", "Reclamo.txt"),
    "sugerencia": ("Sugerencia", "Sugerencia.txt"),
}
CAMPOS_REGISTRO = (
    "tipo_solicitud",
    "nombre_completo",
    "tipo_documento",
    "numero_documento",
    "tipo_telefono",
    "telefono_contacto",
    "correo_electronico",
    "direccion",
    "fecha_radicacion",
    "canal_recepcion",
    "asunto_titulo",
    "descripcion_detallada",
    "tipo_mascota",
    "campus_relacionado",
    "fecha_max_respuesta",
    "estado_peticion",
    "fecha_solucion",
)


def _normalizar_tipo(tipo_solicitud):
    """Devuelve el nombre oficial y el archivo, aceptando el tipo con o sin tilde."""
    if not isinstance(tipo_solicitud, str):
        raise ValueError("El tipo de solicitud debe ser texto.")

    clave = "".join(
        caracter
        for caracter in unicodedata.normalize("NFKD", tipo_solicitud.strip().casefold())
        if not unicodedata.combining(caracter)
    )
    try:
        return ARCHIVOS_POR_TIPO[clave]
    except KeyError as error:
        raise ValueError(f"Tipo de solicitud no válido: {tipo_solicitud}") from error


def _ruta_archivo(tipo_solicitud):
    """Crea la carpeta de datos si hace falta y obtiene el archivo del tipo indicado."""
    _, nombre_archivo = _normalizar_tipo(tipo_solicitud)
    CARPETA_DATA.mkdir(parents=True, exist_ok=True)
    return CARPETA_DATA / nombre_archivo


def _a_texto(valor):
    """Convierte fechas y valores opcionales a una representación de texto estable."""
    if valor is None:
        return ""
    if isinstance(valor, (date, datetime)):
        return valor.isoformat()
    return str(valor)


def _leer_todos(tipo_solicitud):
    """Lee registros completos y conserva tildes, separadores y saltos de línea."""
    ruta = _ruta_archivo(tipo_solicitud)
    if not ruta.exists():
        return []

    registros = []
    with ruta.open("r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo, delimiter=";", quotechar='"')
        for numero_linea, fila in enumerate(lector, start=1):
            if not fila:
                continue
            if len(fila) != len(CAMPOS_REGISTRO) + 1:
                raise ValueError(
                    f"El registro de la línea {numero_linea} en {ruta.name} "
                    "no tiene todos los campos esperados."
                )
            try:
                identificador = int(fila[0])
            except ValueError as error:
                raise ValueError(
                    f"El ID de la línea {numero_linea} en {ruta.name} no es válido."
                ) from error

            registro = {"id": identificador}
            registro.update(dict(zip(CAMPOS_REGISTRO, fila[1:])))
            registros.append(registro)
    return registros


def _guardar_todos(tipo_solicitud, registros):
    """Reescribe un archivo mediante un temporal para evitar dejarlo a medias."""
    ruta = _ruta_archivo(tipo_solicitud)
    temporal = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            newline="",
            dir=CARPETA_DATA,
            delete=False,
        ) as archivo:
            temporal = Path(archivo.name)
            escritor = csv.writer(
                archivo, delimiter=";", quotechar='"', lineterminator="\n"
            )
            for registro in registros:
                escritor.writerow(
                    [registro["id"]]
                    + [_a_texto(registro.get(campo)) for campo in CAMPOS_REGISTRO]
                )
        os.replace(temporal, ruta)
    finally:
        if temporal is not None and temporal.exists():
            temporal.unlink()

def _guardar_copia_semanal(tipo_solicitud, registro):
    """Guarda una PQRS en la carpeta correspondiente a su semana."""

    fecha = registro["fecha_radicacion"]

    # Convertir la fecha al formato que Python puede reconocer
    if isinstance(fecha, (date, datetime)):
        fecha_obj = fecha
    else:
        try:
            fecha_obj = datetime.fromisoformat(str(fecha))
        except ValueError:
            fecha_obj = datetime.strptime(str(fecha), "%d/%m/%Y")

    # Obtener el año y la semana
    anio, semana, _ = fecha_obj.isocalendar()

    # Crear la carpeta del año y de la semana
    carpeta_semana = CARPETA_DATA / str(anio) / f"Semana_{semana:02d}"
    carpeta_semana.mkdir(parents=True, exist_ok=True)

    # Crear los cuatro archivos de la semana
    for _, nombre_archivo in ARCHIVOS_POR_TIPO.values():
        (carpeta_semana / nombre_archivo).touch(exist_ok=True)

    # Identificar el archivo correspondiente al tipo de PQRS
    _, nombre_archivo = _normalizar_tipo(tipo_solicitud)
    ruta_semanal = carpeta_semana / nombre_archivo

    # Guardar el registro en el archivo semanal
    with ruta_semanal.open("a", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(
            archivo, delimiter=";", quotechar='"', lineterminator="\n"
        )
        escritor.writerow(
            [registro["id"]]
            + [_a_texto(registro.get(campo)) for campo in CAMPOS_REGISTRO]
        )


def guardar_registro(tipo_solicitud, datos):
    """Guarda una PQRS y devuelve su ID consecutivo independiente por archivo."""
    tipo_oficial, _ = _normalizar_tipo(tipo_solicitud)
    registros = _leer_todos(tipo_oficial)
    nuevo_id = max((registro["id"] for registro in registros), default=0) + 1

    nuevo = {campo: "" for campo in CAMPOS_REGISTRO}
    nuevo.update({campo: datos[campo] for campo in CAMPOS_REGISTRO if campo in datos})
    nuevo["tipo_solicitud"] = tipo_oficial
    nuevo["estado_peticion"] = nuevo.get("estado_peticion") or "Registrada"
    nuevo["fecha_solucion"] = nuevo.get("fecha_solucion") or ""
    registros.append({"id": nuevo_id, **nuevo})
    _guardar_todos(tipo_oficial, registros)
    _guardar_copia_semanal(tipo_oficial, {"id": nuevo_id, **nuevo})
    return nuevo_id


def leer_lineas_archivo(ruta):
    """Lee las líneas de una ruta de texto; devuelve una lista vacía si no existe."""
    ruta = Path(ruta)
    if not ruta.is_absolute():
        ruta = Path(__file__).resolve().parent.parent / ruta
    try:
        with ruta.open("r", encoding="utf-8", newline="") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        return []


def leer_registros(tipo_solicitud, llaves=None):
    """Lee registros de un tipo; `llaves` permite solicitar un subconjunto de campos."""
    registros = _leer_todos(tipo_solicitud)
    if llaves is None:
        return registros
    campos = list(llaves)
    return [
        {"id": registro["id"], **{campo: registro.get(campo, "") for campo in campos}}
        for registro in registros
    ]


def leer_todos_registros():
    """Lee y combina los registros de los cuatro archivos, conservando su tipo."""
    return [
        registro
        for tipo, _ in ARCHIVOS_POR_TIPO.values()
        for registro in _leer_todos(tipo)
    ]


def obtener_registro(tipo_solicitud, id_buscar):
    """Busca un registro por su ID dentro del archivo de su tipo."""
    return next(
        (
            registro
            for registro in _leer_todos(tipo_solicitud)
            if registro["id"] == int(id_buscar)
        ),
        None,
    )


def actualizar_datos(tipo_solicitud, id_buscar, cambios):
    """Actualiza solo los campos indicados y devuelve si encontró el registro."""
    registros = _leer_todos(tipo_solicitud)
    for registro in registros:
        if registro["id"] == int(id_buscar):
            for campo, valor in cambios.items():
                if campo in CAMPOS_REGISTRO:
                    registro[campo] = _a_texto(valor)
            _guardar_todos(tipo_solicitud, registros)
            return True
    return False


def actualizar_registro(tipo_solicitud, id_buscar, llaves, datos_nuevos):
    """Mantiene la interfaz previa de actualización por lista de campos."""
    cambios = {
        llave: datos_nuevos[llave]
        for llave in llaves
        if llave in datos_nuevos
    }
    return actualizar_datos(tipo_solicitud, id_buscar, cambios)
