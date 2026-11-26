"""Validaciones para los datos de PatiTrack."""

import re
from datetime import date, datetime

TIPOS_DOCUMENTO = ("CC", "TI", "CE", "PP", "NIT")
TIPOS_TELEFONO = ("Celular", "Fijo", "Corporativo", "Otro")
TIPOS_SOLICITUD = ("Petición", "Queja", "Reclamo", "Sugerencia")
CANALES_RECEPCION = (
    "Presencial",
    "Correo electrónico",
    "Página web",
    "Teléfono",
    "Redes sociales",
    "Otro",
)
TIPOS_MASCOTA = ("Perro", "Gato")
ESTADOS_PQRS = ("Registrada", "En proceso", "Solucionada")
CAMPUS = (
    "Campus Medellín - Ciudad Universitaria",
    "Campus Medellín - Ciudadela Robledo",
    "Campus en el Área de la salud",
    "Campus Medellín - Sede de Posgrado",
    "Campus Medellín - Edificio San Ignacio",
    "Campus Medellín - Antigua Escuela de Derecho",
    "Campus Medellín - Edificio Antioquia",
    "Campus Medellín - Casas Patrimoniales",
    "Campus Medellín - Edificio de Extensión",
)

FORMATO_FECHA = "%d/%m/%Y"
CARACTERES_NOMBRE = " '-"
CARACTERES_DIRECCION = " #-/.,"
CARACTERES_ASUNTO = " .,;:!?¿¡()[]'\"-_/"


def _validar_opcion(valor, opciones, nombre_campo):
    """Valida una opción y devuelve su forma oficial, uniforme y legible."""
    if not isinstance(valor, str):
        return None, f"{nombre_campo} debe ser texto."

    valor_limpio = valor.strip()
    for opcion in opciones:
        if valor_limpio.casefold() == opcion.casefold():
            return opcion, ""

    opciones_texto = ", ".join(opciones)
    return None, f"{nombre_campo} debe ser una de estas opciones: {opciones_texto}."


def validar_nombre(nombre):
    """Valida nombres completos con letras, espacios, apóstrofes y guiones."""
    if not isinstance(nombre, str):
        return None, "El nombre debe ser texto."

    nombre_limpio = nombre.strip()
    if not 3 <= len(nombre_limpio) <= 100:
        return None, "El nombre debe tener entre 3 y 100 caracteres."

    if not any(caracter.isalpha() for caracter in nombre_limpio):
        return None, "El nombre debe contener letras."

    if any(
        not (caracter.isalpha() or caracter in CARACTERES_NOMBRE)
        for caracter in nombre_limpio
    ):
        return None, "El nombre solo puede incluir letras, espacios, apóstrofes y guiones."

    return nombre_limpio, ""


def validar_tipo_documento(tipo_documento):
    """Valida y normaliza el tipo de documento admitido."""
    return _validar_opcion(tipo_documento, TIPOS_DOCUMENTO, "El tipo de documento")


def validar_numero_documento(numero_documento):
    """Valida un número de documento de 3 a 15 dígitos ASCII."""
    if not isinstance(numero_documento, str):
        return None, "El número de documento debe ingresarse como texto numérico."

    numero_limpio = numero_documento.strip()
    if not (numero_limpio.isascii() and numero_limpio.isdigit()):
        return None, "El número de documento solo puede contener dígitos."
    if not 3 <= len(numero_limpio) <= 15:
        return None, "El número de documento debe tener entre 3 y 15 dígitos."

    return numero_limpio, ""


def validar_tipo_telefono(tipo_telefono):
    """Valida y normaliza el tipo de teléfono admitido."""
    return _validar_opcion(tipo_telefono, TIPOS_TELEFONO, "El tipo de teléfono")


def validar_telefono(telefono):
    """Valida un teléfono de contacto de exactamente 10 dígitos ASCII."""
    if not isinstance(telefono, str):
        return None, "El teléfono debe ingresarse como texto numérico."

    telefono_limpio = telefono.strip()
    if not (telefono_limpio.isascii() and telefono_limpio.isdigit()):
        return None, "El teléfono solo puede contener dígitos."
    if len(telefono_limpio) != 10:
        return None, "El teléfono debe tener exactamente 10 dígitos."

    return telefono_limpio, ""


def validar_correo(correo):
    """Valida el formato básico del correo y su longitud máxima."""
    if not isinstance(correo, str):
        return None, "El correo electrónico debe ser texto."

    correo_limpio = correo.strip()
    if len(correo_limpio) > 254:
        return None, "El correo electrónico no puede superar 254 caracteres."
    if correo_limpio.count("@") != 1:
        return None, "El correo electrónico debe contener un único símbolo @."

    parte_local, dominio = correo_limpio.split("@")
    if not parte_local or len(parte_local) > 64 or not dominio:
        return None, "El correo debe tener texto antes de @ y un dominio válido."
    if parte_local.startswith(".") or parte_local.endswith(".") or ".." in parte_local:
        return None, "La parte inicial del correo tiene puntos en una posición inválida."

    caracteres_locales = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!#$%&'*+/=?^_`{|}~-")
    if any(caracter not in caracteres_locales for caracter in parte_local):
        return None, "La parte inicial del correo contiene caracteres no permitidos."

    etiquetas_dominio = dominio.split(".")
    if len(etiquetas_dominio) < 2:
        return None, "El dominio debe incluir al menos un punto, como correo.com."
    for etiqueta in etiquetas_dominio:
        if not etiqueta or len(etiqueta) > 63:
            return None, "El dominio del correo tiene una sección vacía o demasiado larga."
        if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?", etiqueta):
            return None, "El dominio contiene caracteres o guiones en una posición inválida."

    return correo_limpio, ""


def validar_direccion(direccion):
    """Valida una dirección opcional y devuelve texto limpio."""
    if not isinstance(direccion, str):
        return None, "La dirección debe ingresarse como texto."

    direccion_limpia = direccion.strip()
    if direccion_limpia == "":
        return "", ""
    if not 5 <= len(direccion_limpia) <= 200:
        return None, "La dirección debe tener entre 5 y 200 caracteres."

    if any(
        not (caracter.isalpha() or caracter.isdigit() or caracter in CARACTERES_DIRECCION)
        for caracter in direccion_limpia
    ):
        return None, "La dirección solo puede incluir letras, números, espacios y # - . / ,"

    return direccion_limpia, ""


def validar_fecha_radicacion(fecha_radicacion):
    """Valida una fecha DD/MM/AAAA y rechaza fechas posteriores a hoy."""
    if isinstance(fecha_radicacion, datetime):
        fecha_limpia = fecha_radicacion.date()
    elif isinstance(fecha_radicacion, date):
        fecha_limpia = fecha_radicacion
    elif isinstance(fecha_radicacion, str):
        try:
            fecha_limpia = datetime.strptime(fecha_radicacion.strip(), FORMATO_FECHA).date()
        except ValueError:
            return None, "La fecha debe tener el formato DD/MM/AAAA y ser válida."
    else:
        return None, "La fecha de radicación debe ser una fecha o un texto DD/MM/AAAA."

    if fecha_limpia > date.today():
        return None, "La fecha de radicación no puede estar en el futuro."

    return fecha_limpia, ""


def validar_tipo_solicitud(tipo_solicitud):
    """Valida y normaliza el tipo de solicitud PQRS."""
    return _validar_opcion(tipo_solicitud, TIPOS_SOLICITUD, "El tipo de solicitud")


def validar_canal_recepcion(canal_recepcion):
    """Valida y normaliza el canal de recepción."""
    return _validar_opcion(canal_recepcion, CANALES_RECEPCION, "El canal de recepción")


def validar_asunto(asunto):
    """Valida el asunto obligatorio y sus signos de puntuación básicos."""
    if not isinstance(asunto, str):
        return None, "El asunto debe ser texto."

    asunto_limpio = asunto.strip()
    if not 5 <= len(asunto_limpio) <= 150:
        return None, "El asunto debe tener entre 5 y 150 caracteres."
    if any(
        not (caracter.isalpha() or caracter.isdigit() or caracter.isspace() or caracter in CARACTERES_ASUNTO)
        for caracter in asunto_limpio
    ):
        return None, "El asunto contiene caracteres no permitidos."

    return asunto_limpio, ""


def validar_descripcion(descripcion):
    """Valida la descripción detallada, obligatoria y de longitud limitada."""
    if not isinstance(descripcion, str):
        return None, "La descripción debe ser texto."

    descripcion_limpia = descripcion.strip()
    if not 20 <= len(descripcion_limpia) <= 2000:
        return None, "La descripción debe tener entre 20 y 2000 caracteres."

    return descripcion_limpia, ""


def validar_tipo_mascota(tipo_mascota):
    """Valida y normaliza el tipo de mascota relacionada."""
    return _validar_opcion(tipo_mascota, TIPOS_MASCOTA, "El tipo de mascota")


def validar_campus(campus):
    """Valida y normaliza el campus relacionado con la PQRS."""
    return _validar_opcion(campus, CAMPUS, "El campus")


def validar_estado(estado):
    """Valida que el estado pertenezca a los estados definidos para PQRS."""
    return _validar_opcion(estado, ESTADOS_PQRS, "El estado")
