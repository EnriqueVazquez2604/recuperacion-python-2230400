from examen_recuperacion_2230400.models import Unidad
from examen_recuperacion_2230400.services import (
    calcular_lugares_disponibles,
    mostrar_unidades,
    mostrar_unidades_llenas,
    registrar_unidad,
    resumen_general,
    unidad_mayor_ocupacion,
)


def main():
    unidades = []

    # Ejemplo de registro
    registrar_unidad(unidades, Unidad(1, "Carlos", 20, 18, "Ruta Norte"))
    registrar_unidad(unidades, Unidad(2, "Ana", 15, 15, "Ruta Sur"))
    registrar_unidad(unidades, Unidad(3, "Luis", 25, 10, "Ruta Centro"))

    print("Todas las unidades:")
    print(mostrar_unidades(unidades))

    print("\nLugares disponibles:")
    print(calcular_lugares_disponibles(unidades))

    print("\nUnidades llenas:")
    print(mostrar_unidades_llenas(unidades))

    print("\nUnidad con mayor ocupación:")
    print(unidad_mayor_ocupacion(unidades))

    print("\nResumen general:")
    print(resumen_general(unidades))


if __name__ == "__main__":
    main()
