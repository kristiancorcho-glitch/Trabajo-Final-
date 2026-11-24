"""Generación del comprobante de radicación en formato ASCII de 120 columnas."""

import unicodedata
from datetime import date
from textwrap import wrap


ANCHO_COMPROBANTE = 120
ANCHO_INTERIOR = ANCHO_COMPROBANTE - 4


def _ascii(texto):
    """Quita tildes y caracteres no ASCII para el comprobante de consola."""
    normalizado = unicodedata.normalize("NFKD", str(texto))
    return "".join(
        caracter for caracter in normalizado
        if not unicodedata.combining(caracter)
    ).encode("ascii", "ignore").decode("ascii")


def _fecha_legible(valor):
    """Muestra fechas ISO como DD/MM/AAAA y conserva el valor si no se reconoce."""
    if not valor:
        return "N/A"
    texto = str(valor)
    try:
        return date.fromisoformat(texto[:10]).strftime("%d/%m/%Y")
    except ValueError:
        return texto


def generar_comprobante(registro):
    """Devuelve el comprobante; excluye la descripción y garantiza líneas de 120."""
    tipo = registro.get("tipo_solicitud", "PQRS")
    identificador = registro.get("id", registro.get("id_registro", "N/A"))
    campos = (
        (
            "Radicado",
            f"{tipo.upper()}-{int(identificador):06d}"
            if str(identificador).isdigit()
            else identificador,
        ),
        ("Solicitante", registro.get("nombre_completo", "N/A")),
        ("Documento", f"{registro.get('tipo_documento', 'N/A')} {registro.get('numero_documento', '')}"),
        ("Telefono", f"{registro.get('tipo_telefono', 'N/A')} - {registro.get('telefono_contacto', 'N/A')}"),
        ("Correo", registro.get("correo_electronico", "N/A")),
        ("Direccion", registro.get("direccion") or "N/A"),
        ("Fecha de radicacion", _fecha_legible(registro.get("fecha_radicacion"))),
        ("Canal de recepcion", registro.get("canal_recepcion", "N/A")),
        ("Asunto", registro.get("asunto_titulo", "N/A")),
        ("Mascota", registro.get("tipo_mascota", "N/A")),
        ("Campus", registro.get("campus_relacionado", "N/A")),
        ("Fecha maxima de respuesta", _fecha_legible(registro.get("fecha_max_respuesta"))),
        ("Estado", registro.get("estado_peticion", "Registrada")),
        ("Fecha de solucion", _fecha_legible(registro.get("fecha_solucion"))),
    )

    borde = "+" + "-" * (ANCHO_COMPROBANTE - 2) + "+"
    titulo = " PATITRACK - COMPROBANTE DE RADICACION ".center(
        ANCHO_COMPROBANTE - 2
    )
    lineas = [borde, f"|{titulo}|", borde]
    for etiqueta, valor in campos:
        texto = _ascii(f"{etiqueta}: {valor}")
        fragmentos = wrap(texto, width=ANCHO_INTERIOR) or [""]
        lineas.extend("| " + fragmento.ljust(ANCHO_INTERIOR) + " |" for fragmento in fragmentos)
    lineas.append(borde)
    return "\n".join(lineas)
