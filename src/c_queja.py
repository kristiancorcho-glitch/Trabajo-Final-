"""Clase concreta, para una queja."""

from .c_pqrs import c_pqrs


class c_Queja(c_pqrs):
    """Representa una queja con los campos comunes de una PQRS."""

    tipo_solicitud = "Queja"
