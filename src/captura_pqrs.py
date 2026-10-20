"""Captura los datos básicos de la PQRS."""

from datetime import timedelta

from .captura_solicitante import pedir_dato
from .validaciones import (
    TIPOS_SOLICITUD,
    validar_fecha_radicacion,
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


def capturar_datos_pqrs():
    """Captura el tipo de solicitud y sus fechas de radicación y respuesta."""
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

    return {
        "tipo_solicitud": tipo_solicitud,
        "fecha_radicacion": fecha_radicacion,
        "fecha_max_respuesta": fecha_max_respuesta,
    }


def mostrar_datos_pqrs(datos):
    """Muestra el tipo de PQRS y las fechas calculadas."""
    print("\nINFORMACIÓN DE LA PQRS")
    print("-" * 50)
    print(f"Tipo de solicitud:       {datos['tipo_solicitud']}")
    print(f"Fecha de radicación:     {datos['fecha_radicacion']:%d/%m/%Y}")
    print(f"Fecha máxima respuesta:  {datos['fecha_max_respuesta']:%d/%m/%Y}")
