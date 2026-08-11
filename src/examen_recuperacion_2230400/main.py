from examen_recuperacion_2230400.models import Unidad
from examen_recuperacion_2230400.services import (
    registrar_unidad,
    mostrar_unidades,
    calcular_lugares_disponibles,
    mostrar_unidades_llenas,
    unidad_mayor_ocupacion,
    resumen_general,
)


def mostrar_unidad(unidad):
    return f"Unidad {unidad.numero} | Conductor: {unidad.conductor} | Capacidad: {unidad.capacidad} | Pasajeros: {unidad.pasajeros} | Ruta: {unidad.ruta}"


def main():
    unidades = []

    # Ejemplo de registro
    registrar_unidad(unidades, Unidad(1, "Carlos", 20, 18, "Ruta Norte"))
    registrar_unidad(unidades, Unidad(2, "Ana", 15, 15, "Ruta Sur"))
    registrar_unidad(unidades, Unidad(3, "Luis", 25, 10, "Ruta Centro"))

    print("=== Todas las unidades ===")
    for u in mostrar_unidades(unidades):
        print(mostrar_unidad(u))

    print("\n=== Lugares disponibles ===")
    for d in calcular_lugares_disponibles(unidades):
        print(f"Unidad {d['numero']} → {d['disponibles']} lugares libres")

    print("\n=== Unidades llenas ===")
    for u in mostrar_unidades_llenas(unidades):
        print(mostrar_unidad(u))

    print("\n=== Unidad con mayor ocupación ===")
    mayor = unidad_mayor_ocupacion(unidades)
    if mayor:
        print(mostrar_unidad(mayor))

    print("\n=== Resumen general ===")
    resumen = resumen_general(unidades)
    print(f"Total de unidades: {resumen['total_unidades']}")
    print(f"Promedio de ocupación: {resumen['promedio_ocupacion']:.2f} pasajeros")


if __name__ == "__main__":
    main()
