"""Menú inicial, de PatiTrack."""

from .captura_pqrs import capturar_datos_pqrs, mostrar_datos_pqrs
from .captura_solicitante import (
    capturar_datos_solicitante,
    mostrar_datos_solicitante,
)


def mostrar_menu():
    """Muestra las opciones principales, claras y numeradas."""
    print("\n" + "=" * 42)
    print("           PATITRACK - GESTOR PQRS")
    print("=" * 42)
    print("1. Registrar PQRS")
    print("2. Consultar PQRS")
    print("3. Cambiar estado de una PQRS")
    print("4. Ver estadísticas")
    print("5. Salir")
    print("=" * 42)


def ejecutar_menu():
    """Controla el ciclo principal, sencillo y continuo, del menú."""
    while True:
        mostrar_menu()
        opcion = input("Escriba el número de la opción (1-5): ").strip()

        if opcion == "5":
            print("Gracias por usar PatiTrack.")
            break

        if opcion == "1":
            datos_solicitante = capturar_datos_solicitante()
            datos_pqrs = capturar_datos_pqrs()
            mostrar_datos_solicitante(datos_solicitante)
            mostrar_datos_pqrs(datos_pqrs)
            print(
                "\nDatos del solicitante y de la PQRS validados. La captura del detalle "
                "completo y su almacenamiento se añadirán en versiones posteriores."
            )
        elif opcion in ("2", "3", "4"):
            print("Esta función se implementará en una versión posterior.")
        else:
            print("Opción inválida. Ingrese un número del 1 al 5.")


if __name__ == "__main__":
    ejecutar_menu()
