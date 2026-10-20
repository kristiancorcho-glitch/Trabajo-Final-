"""Clase concreta, para un reclamo."""

from .c_pqrs import c_pqrs


class c_Reclamo(c_pqrs):
    """Representa un reclamo con los campos comunes de una PQRS."""

    tipo_solicitud = "Reclamo"
