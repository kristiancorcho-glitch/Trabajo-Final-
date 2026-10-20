"""Modelo base, para una solicitud PQRS."""


class c_pqrs:
    """Contiene los datos comunes, claros y consistentes de una PQRS."""

    tipo_solicitud = ""

    def __init__(
        self,
        id_registro=None,
        nombre_completo="",
        tipo_documento="",
        numero_documento="",
        tipo_telefono="",
        telefono_contacto="",
        correo_electronico="",
        direccion="",
        fecha_radicacion=None,
        canal_recepcion="",
        asunto_titulo="",
        descripcion_detallada="",
        tipo_mascota="",
        campus_relacionado="",
        fecha_max_respuesta=None,
    ):
        """Inicializa los datos completos y compartidos de la solicitud."""
        self.id_registro = id_registro
        self.nombre_completo = nombre_completo
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.tipo_telefono = tipo_telefono
        self.telefono_contacto = telefono_contacto
        self.correo_electronico = correo_electronico
        self.direccion = direccion
        self.fecha_radicacion = fecha_radicacion
        self.canal_recepcion = canal_recepcion
        self.asunto_titulo = asunto_titulo
        self.descripcion_detallada = descripcion_detallada
        self.tipo_mascota = tipo_mascota
        self.campus_relacionado = campus_relacionado
        self.fecha_max_respuesta = fecha_max_respuesta
        self.estado_peticion = "Registrada"
        self.fecha_solucion = None
