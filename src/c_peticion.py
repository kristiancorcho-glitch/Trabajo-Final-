"""Clase concreta, para una petición."""

from .c_pqrs import c_pqrs


class c_Peticion(c_pqrs):
    """Representa una petición con los campos comunes de una PQRS."""

    tipo_solicitud = "Petición"


# Alias para conservar compatibilidad con el nombre usado en prototipos previos.
c_peticion = c_Peticion
