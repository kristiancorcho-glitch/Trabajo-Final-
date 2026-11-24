"""Cálculo de estadísticas para los registros PQRS."""

from collections import Counter
from datetime import date, datetime, timedelta


DIAS_PROXIMOS_A_VENCER = 5
ESTADO_SOLUCIONADA = "Solucionada"


def _obtener(registro, campo, predeterminado=None):
    """Lee un campo desde un diccionario o desde un objeto PQRS."""
    if isinstance(registro, dict):
        return registro.get(campo, predeterminado)
    return getattr(registro, campo, predeterminado)


def _convertir_fecha(valor):
    """Normaliza fechas date, datetime o texto DD/MM/AAAA/AAAA-MM-DD."""
    if isinstance(valor, datetime):
        return valor.date()
    if isinstance(valor, date):
        return valor
    if isinstance(valor, str):
        for formato in ("%d/%m/%Y", "%Y-%m-%d"):
            try:
                return datetime.strptime(valor.strip(), formato).date()
            except ValueError:
                continue
    return None


def calcular_promedio_dias_respuesta(registros):
    """Promedia los días de respuesta de PQRS solucionadas con fechas válidas."""
    duraciones = []
    for registro in registros:
        estado = str(_obtener(registro, "estado_peticion", "") or "").casefold()
        if estado != ESTADO_SOLUCIONADA.casefold():
            continue

        fecha_inicio = _convertir_fecha(_obtener(registro, "fecha_radicacion"))
        fecha_fin = _convertir_fecha(_obtener(registro, "fecha_solucion"))
        if fecha_inicio and fecha_fin and fecha_fin >= fecha_inicio:
            duraciones.append((fecha_fin - fecha_inicio).days)

    if not duraciones:
        return None
    return sum(duraciones) / len(duraciones)


def _contar_por_campo(registros, campo):
    """Cuenta las categorías de un campo, ignorando valores vacíos."""
    valores = (
        _obtener(registro, campo)
        for registro in registros
    )
    return dict(sorted(Counter(valor for valor in valores if valor).items()))


def obtener_pqrs_mas_antigua_pendiente(registros):
    """Devuelve la PQRS pendiente más antigua, o None si no hay pendientes."""
    pendientes = [
        registro
        for registro in registros
        if str(_obtener(registro, "estado_peticion", "Registrada") or "").casefold()
        != ESTADO_SOLUCIONADA.casefold()
        and _convertir_fecha(_obtener(registro, "fecha_radicacion")) is not None
    ]
    if not pendientes:
        return None
    return min(
        pendientes,
        key=lambda registro: _convertir_fecha(
            _obtener(registro, "fecha_radicacion")
        ),
    )


def obtener_pqrs_proximas_a_vencer(registros, hoy=None):
    """Lista PQRS pendientes cuyo vencimiento ocurre entre hoy y los próximos 5 días."""
    fecha_actual = hoy or date.today()
    fecha_limite = fecha_actual + timedelta(days=DIAS_PROXIMOS_A_VENCER)
    proximas = []
    for registro in registros:
        estado = str(
            _obtener(registro, "estado_peticion", "Registrada") or ""
        ).casefold()
        fecha_maxima = _convertir_fecha(_obtener(registro, "fecha_max_respuesta"))
        if (
            estado != ESTADO_SOLUCIONADA.casefold()
            and fecha_maxima is not None
            and fecha_actual <= fecha_maxima <= fecha_limite
        ):
            proximas.append(registro)
    return proximas


def generar_estadisticas(registros, hoy=None):
    """Genera el promedio y cinco resúmenes útiles para el menú de estadísticas."""
    registros = list(registros)
    return {
        "promedio_dias_respuesta": calcular_promedio_dias_respuesta(registros),
        "cantidad_por_tipo_solicitud": _contar_por_campo(
            registros, "tipo_solicitud"
        ),
        "cantidad_por_tipo_mascota": _contar_por_campo(registros, "tipo_mascota"),
        "pqrs_mas_antigua_pendiente": obtener_pqrs_mas_antigua_pendiente(registros),
        "pqrs_proximas_a_vencer": obtener_pqrs_proximas_a_vencer(registros, hoy),
        "cantidad_por_campus": _contar_por_campo(registros, "campus_relacionado"),
    }
