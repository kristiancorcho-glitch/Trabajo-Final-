"""Clase concreta, para una sugerencia."""

from .c_pqrs import c_pqrs


class c_Sugerencia(c_pqrs):
    """Representa una sugerencia con los campos comunes de una PQRS."""

    tipo_solicitud = "Sugerencia"
