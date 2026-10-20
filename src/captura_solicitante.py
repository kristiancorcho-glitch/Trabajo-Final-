"""Captura ordenada y validada de los datos del solicitante."""

from .validaciones import (
    validar_correo,
    validar_direccion,
    validar_nombre,
    validar_numero_documento,
    validar_telefono,
    validar_tipo_documento,
    validar_tipo_telefono,
)


def pedir_dato(mensaje, funcion_validacion):
    """Solicita un dato hasta recibir una respuesta válida y normalizada."""
    while True:
        entrada = input(mensaje)
        valor_validado, mensaje_error = funcion_validacion(entrada)
        if not mensaje_error:
            return valor_validado
        print(f"Error: {mensaje_error}\n")


def capturar_datos_solicitante():
    """Captura los campos del solicitante y los devuelve en un diccionario."""
    print("\nDATOS DEL SOLICITANTE")

    datos = {
        "nombre_completo": pedir_dato("Ingrese su nombre completo: ", validar_nombre),
        "tipo_documento": pedir_dato(
            "Tipo de documento (CC, TI, CE, PP, NIT): ", validar_tipo_documento
        ),
        "numero_documento": pedir_dato(
            "Ingrese número de documento: ", validar_numero_documento
        ),
        "tipo_telefono": pedir_dato(
            "Tipo de teléfono (Celular, Fijo, Corporativo, Otro): ",
            validar_tipo_telefono,
        ),
        "telefono_contacto": pedir_dato(
            "Ingrese teléfono de contacto (10 dígitos): ", validar_telefono
        ),
        "correo_electronico": pedir_dato(
            "Ingrese su correo electrónico: ", validar_correo
        ),
        "direccion": pedir_dato(
            "Ingrese dirección (opcional; Enter para omitir): ", validar_direccion
        ),
    }

    return datos


def mostrar_datos_solicitante(datos):
    """Muestra un resumen ordenado y legible de los datos validados."""
    direccion = datos["direccion"] if datos["direccion"] else "N/A"

    print("\nDATOS DEL SOLICITANTE")
    print("-" * 50)
    print(f"Nombre completo:     {datos['nombre_completo']}")
    print(
        "Documento:           "
        f"{datos['tipo_documento']} - {datos['numero_documento']}"
    )
    print(
        "Teléfono:            "
        f"{datos['tipo_telefono']} - {datos['telefono_contacto']}"
    )
    print(f"Correo electrónico:  {datos['correo_electronico']}")
    print(f"Dirección:           {direccion}")
