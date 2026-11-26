"""Captura y muestra la información completa de una PQRS."""

import textwrap
from datetime import timedelta

from .captura_solicitante import pedir_dato
from .validaciones import (
    CAMPUS,
    CANALES_RECEPCION,
    TIPOS_MASCOTA,
    TIPOS_SOLICITUD,
    validar_asunto,
    validar_campus,
    validar_canal_recepcion,
    validar_descripcion,
    validar_fecha_radicacion,
    validar_tipo_mascota,
    validar_tipo_solicitud,
)


def _validar_seleccion_tipo_solicitud(seleccion):
    """Convierte una opción numerada en el tipo oficial de solicitud."""
    if not isinstance(seleccion, str):
        return None, "Seleccione un número del 1 al 4."

    seleccion_limpia = seleccion.strip()
    if seleccion_limpia not in ("1", "2", "3", "4"):
        return None, "Seleccione un número del 1 al 4."

    tipo_solicitud = TIPOS_SOLICITUD[int(seleccion_limpia) - 1]
    return validar_tipo_solicitud(tipo_solicitud)


def _crear_validador_seleccion(opciones, validador, nombre_campo):
    """Permite elegir una opción de una lista numerada."""
    def validar_seleccion(seleccion):
        if not isinstance(seleccion, str):
            return None, f"Seleccione un número del 1 al {len(opciones)}."

        seleccion_limpia = seleccion.strip()
        if not seleccion_limpia.isdigit():
            return None, f"Seleccione un número del 1 al {len(opciones)}."

        indice = int(seleccion_limpia) - 1
        if not 0 <= indice < len(opciones):
            return None, f"Seleccione un número del 1 al {len(opciones)}."

        valor, error = validador(opciones[indice])
        if error:
            return None, f"No se pudo validar {nombre_campo.lower()}: {error}"
        return valor, ""

    return validar_seleccion


def _mostrar_opciones(opciones):
    """Imprime opciones numeradas para facilitar la captura."""
    return ", ".join(
        f"{indice}. {opcion}" for indice, opcion in enumerate(opciones, start=1)
    )


def capturar_datos_pqrs():
    """Captura los datos de la solicitud, sus fechas y su contexto."""
    print("\nINFORMACIÓN DE LA PQRS")

    tipo_solicitud = pedir_dato(
        "Tipo de solicitud (1. Petición, 2. Queja, 3. Reclamo, 4. Sugerencia): ",
        _validar_seleccion_tipo_solicitud,
    )
    fecha_radicacion = pedir_dato(
        "Ingrese fecha de radicación (DD/MM/AAAA): ",
        validar_fecha_radicacion,
    )
    fecha_max_respuesta = fecha_radicacion + timedelta(days=30)
    print("\nCanales de recepción:")
    for indice, canal in enumerate(CANALES_RECEPCION, start=1):
        print(f"{indice}. {canal}")
    canal_recepcion = pedir_dato(
        "Favor seleccione el número del canal de recepción: ",
        _crear_validador_seleccion(
            CANALES_RECEPCION,
            validar_canal_recepcion,
            "el canal de recepción",
        ),
    )
    asunto_titulo = pedir_dato("Asunto o título: ", validar_asunto)
    print(
        "Puede consultar los servicios del Hospital Veterinario de la UdeA en:\n"
        "https://www.udea.edu.co/wps/portal/udea/web/inicio/unidades-academicas/"
        "ciencias-agrarias/hospital-veterinario/servicios"
    )
    descripcion_detallada = pedir_dato(
        "Descripción detallada de la solicitud: ", validar_descripcion
    )
    tipo_mascota = pedir_dato(
        f"Tipo de mascota ({_mostrar_opciones(TIPOS_MASCOTA)}): ",
        _crear_validador_seleccion(
            TIPOS_MASCOTA, validar_tipo_mascota, "el tipo de mascota"
        ),
    )
    campus_relacionado = pedir_dato(
        f"Campus relacionado ({_mostrar_opciones(CAMPUS)}): ",
        _crear_validador_seleccion(CAMPUS, validar_campus, "el campus"),
    )

    return {
        "tipo_solicitud": tipo_solicitud,
        "fecha_radicacion": fecha_radicacion,
        "fecha_max_respuesta": fecha_max_respuesta,
        "canal_recepcion": canal_recepcion,
        "asunto_titulo": asunto_titulo,
        "descripcion_detallada": descripcion_detallada,
        "tipo_mascota": tipo_mascota,
        "campus_relacionado": campus_relacionado,
    }


def mostrar_datos_pqrs(datos):
    """Muestra los datos capturados de la PQRS."""
    print("\nINFORMACIÓN DE LA PQRS")
    print("-" * 50)
    print(f"Tipo de solicitud:       {datos['tipo_solicitud']}")
    print(f"Fecha de radicación:     {datos['fecha_radicacion']:%d/%m/%Y}")
    print(f"Fecha máxima respuesta:  {datos['fecha_max_respuesta']:%d/%m/%Y}")
    print(f"Canal de recepción:      {datos['canal_recepcion']}")
    print(f"Asunto:                  {datos['asunto_titulo']}")
    print("Descripción:")
    print(
        textwrap.fill(
            datos["descripcion_detallada"],
            width=70,
            initial_indent="    ",
            subsequent_indent="    ",
        )
    )
    print(f"Tipo de mascota:         {datos['tipo_mascota']}")
    print(f"Campus relacionado:      {datos['campus_relacionado']}")
