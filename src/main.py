"""Menú principal de PatiTrack y coordinación de sus operaciones."""

from datetime import date

from .archivos import (
    actualizar_datos,
    guardar_registro,
    leer_todos_registros,
    obtener_registro,
)
from .c_peticion import c_Peticion
from .c_queja import c_Queja
from .c_reclamo import c_Reclamo
from .c_sugerencia import c_Sugerencia
from .captura_pqrs import capturar_datos_pqrs, mostrar_datos_pqrs
from .captura_solicitante import (
    capturar_datos_solicitante,
    mostrar_datos_solicitante,
)
from .comprobantes import generar_comprobante
from .reportes import generar_estadisticas
from .validaciones import ESTADOS_PQRS, TIPOS_SOLICITUD

MODELOS_POR_TIPO = {
    "Petición": c_Peticion,
    "Queja": c_Queja,
    "Reclamo": c_Reclamo,
    "Sugerencia": c_Sugerencia,
}


def mostrar_menu():
    """Muestra las opciones principales del sistema."""
    print("\n" + "=" * 42)
    print("           PATITRACK - GESTOR PQRS")
    print("=" * 42)
    print("1. Registrar PQRS")
    print("2. Consultar PQRS")
    print("3. Cambiar estado de una PQRS")
    print("4. Ver estadísticas")
    print("5. Salir")
    print("=" * 42)


def _seleccionar_tipo():
    """Solicita el tipo de PQRS para buscarla en su archivo independiente."""
    print("\nSeleccione el tipo de solicitud:")
    for indice, tipo in enumerate(TIPOS_SOLICITUD, start=1):
        print(f"{indice}. {tipo}")
    while True:
        opcion = input("Opción (1-4): ").strip()
        if opcion in ("1", "2", "3", "4"):
            return TIPOS_SOLICITUD[int(opcion) - 1]
        print("Opción inválida. Ingrese un número del 1 al 4.")


def _pedir_id():
    """Solicita un identificador numérico positivo."""
    while True:
        identificador = input("Ingrese el ID de la PQRS: ").strip()
        if identificador.isascii() and identificador.isdigit() and int(identificador) > 0:
            return int(identificador)
        print("El ID debe ser un número entero positivo.")


def _fecha_mostrar(valor):
    """Convierte una fecha almacenada en ISO a formato DD/MM/AAAA."""
    if not valor:
        return "N/A"
    try:
        return date.fromisoformat(str(valor)[:10]).strftime("%d/%m/%Y")
    except ValueError:
        return str(valor)


def _mostrar_resumen(registro):
    """Imprime los campos principales de una PQRS recuperada del archivo."""
    print("\n" + "-" * 60)
    print(f"Radicado:                {registro['tipo_solicitud']} - {registro['id']}")
    print(f"Solicitante:             {registro.get('nombre_completo') or 'N/A'}")
    print(f"Documento:               {registro.get('tipo_documento') or 'N/A'} - "
        f"{registro.get('numero_documento') or 'N/A'}")
    print(f"Teléfono:                {registro.get('telefono_contacto') or 'N/A'}")
    print(f"Correo:                  {registro.get('correo_electronico') or 'N/A'}")
    print(f"Dirección:               {registro.get('direccion') or 'N/A'}")
    print(f"Fecha de radicación:     {_fecha_mostrar(registro.get('fecha_radicacion'))}")
    print(f"Canal:                   {registro.get('canal_recepcion') or 'N/A'}")
    print(f"Asunto:                  {registro.get('asunto_titulo') or 'N/A'}")
    print(f"Descripción:             {registro.get('descripcion_detallada') or 'N/A'}")
    print(f"Mascota:                 {registro.get('tipo_mascota') or 'N/A'}")
    print(f"Campus:                  {registro.get('campus_relacionado') or 'N/A'}")
    print(f"Fecha máxima respuesta:  {_fecha_mostrar(registro.get('fecha_max_respuesta'))}")
    print(f"Estado:                  {registro.get('estado_peticion') or 'Registrada'}")
    print(f"Fecha de solución:       {_fecha_mostrar(registro.get('fecha_solucion'))}")
    print("-" * 60)


def registrar_pqrs():
    """Captura y guarda una PQRS, construyendo su objeto de modelo."""
    datos = {**capturar_datos_solicitante(), **capturar_datos_pqrs()}
    tipo_solicitud = datos["tipo_solicitud"]
    modelo = MODELOS_POR_TIPO[tipo_solicitud]
    campos_modelo = {
        campo: datos[campo]
        for campo in (
            "nombre_completo",
            "tipo_documento",
            "numero_documento",
            "tipo_telefono",
            "telefono_contacto",
            "correo_electronico",
            "direccion",
            "fecha_radicacion",
            "canal_recepcion",
            "asunto_titulo",
            "descripcion_detallada",
            "tipo_mascota",
            "campus_relacionado",
            "fecha_max_respuesta",
        )
    }
    solicitud = modelo(**campos_modelo)
    datos_guardar = vars(solicitud).copy()
    datos_guardar.pop("id_registro", None)
    datos_guardar["tipo_solicitud"] = solicitud.tipo_solicitud

    identificador = guardar_registro(tipo_solicitud, datos_guardar)
    solicitud.id_registro = identificador
    registro = {**datos_guardar, "id": identificador}

    mostrar_datos_solicitante(datos)
    mostrar_datos_pqrs(datos)
    print(f"\nPQRS guardada correctamente. Su ID es {identificador}.")
    print(generar_comprobante(registro))


def consultar_pqrs():
    """Busca una PQRS por tipo e ID y permite imprimir su comprobante."""
    tipo = _seleccionar_tipo()
    identificador = _pedir_id()
    registro = obtener_registro(tipo, identificador)
    if registro is None:
        print("No se encontró una PQRS con ese tipo e ID.")
        return

    _mostrar_resumen(registro)
    if input("¿Desea imprimir el comprobante? (S/N): ").strip().casefold() == "s":
        print(generar_comprobante(registro))


def cambiar_estado_pqrs():
    """Avanza una PQRS solo a la siguiente etapa permitida del flujo."""
    tipo = _seleccionar_tipo()
    identificador = _pedir_id()
    registro = obtener_registro(tipo, identificador)
    if registro is None:
        print("No se encontró una PQRS con ese tipo e ID.")
        return

    estado_actual = registro.get("estado_peticion") or ESTADOS_PQRS[0]
    print(f"Estado actual: {estado_actual}")
    if estado_actual == ESTADOS_PQRS[0]:
        siguiente_estado = ESTADOS_PQRS[1]
    elif estado_actual == ESTADOS_PQRS[1]:
        siguiente_estado = ESTADOS_PQRS[2]
    else:
        print("La PQRS ya está solucionada y no admite más cambios de estado.")
        return

    confirmar = input(f"¿Cambiar el estado a «{siguiente_estado}»? (S/N): ")
    if confirmar.strip().casefold() != "s":
        print("No se realizaron cambios.")
        return

    cambios = {"estado_peticion": siguiente_estado}
    if siguiente_estado == ESTADOS_PQRS[2]:
        cambios["fecha_solucion"] = date.today().isoformat()
    if actualizar_datos(tipo, identificador, cambios):
        print(f"Estado actualizado a: {siguiente_estado}")
        if "fecha_solucion" in cambios:
            print(f"Fecha de solución guardada: {date.today():%d/%m/%Y}")
    else:
        print("No fue posible actualizar el registro.")


def _resumen_estadisticas(estadisticas):
    """Presenta en consola el promedio y las cinco estadísticas adicionales."""
    print("\nESTADÍSTICAS DE PATITRACK")
    print("-" * 50)
    promedio = estadisticas["promedio_dias_respuesta"]
    if promedio is None:
        print("Promedio de respuesta: todavía no hay PQRS solucionadas.")
    else:
        print(f"Promedio de días hasta la solución: {promedio:.2f}")

    for titulo, clave in (
        ("PQRS por tipo de solicitud", "cantidad_por_tipo_solicitud"),
        ("PQRS por tipo de mascota", "cantidad_por_tipo_mascota"),
        ("PQRS por campus", "cantidad_por_campus"),
    ):
        conteos = estadisticas[clave]
        print(f"{titulo}: {conteos if conteos else 'Sin registros'}")

    antigua = estadisticas["pqrs_mas_antigua_pendiente"]
    if antigua:
        print(
            "PQRS pendiente más antigua: "
            f"{antigua.get('tipo_solicitud')} #{antigua.get('id')} "
            f"(radicada {_fecha_mostrar(antigua.get('fecha_radicacion'))})"
        )
    else:
        print("PQRS pendiente más antigua: ninguna")

    proximas = estadisticas["pqrs_proximas_a_vencer"]
    print(f"PQRS que vencen en los próximos 5 días: {len(proximas)}")
    for registro in proximas:
        print(
            f"  - {registro.get('tipo_solicitud')} #{registro.get('id')}: "
            f"{_fecha_mostrar(registro.get('fecha_max_respuesta'))}"
        )


def ver_estadisticas():
    """Carga los registros de los cuatro archivos y muestra sus métricas."""
    registros = leer_todos_registros()
    if not registros:
        print("Todavía no hay PQRS guardadas para generar estadísticas.")
        return
    _resumen_estadisticas(generar_estadisticas(registros))


def ejecutar_menu():
    """Ejecuta el menú principal hasta que el usuario elija salir."""
    acciones = {
        "1": registrar_pqrs,
        "2": consultar_pqrs,
        "3": cambiar_estado_pqrs,
        "4": ver_estadisticas,
    }
    while True:
        mostrar_menu()
        opcion = input("Escriba el número de la opción (1-5): ").strip()
        if opcion == "5":
            print("Gracias por usar PatiTrack.")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida. Ingrese un número del 1 al 5.")
            continue
        try:
            accion()
        except (OSError, ValueError) as error:
            print(f"No se pudo completar la operación: {error}")


if __name__ == "__main__":
    ejecutar_menu()
