from examen_recuperacion_2230400.models import Unidad
from examen_recuperacion_2230400.services import (
    calcular_lugares_disponibles,
    mostrar_unidades_llenas,
    unidad_mayor_ocupacion,
)

def main():
    unidades = [
        Unidad(1, "Carlos", 20, 18, "Ruta Norte"),
        Unidad(2, "Ana", 15, 15, "Ruta Sur"),
        Unidad(3, "Luis", 25, 10, "Ruta Centro"),
    ]

    print("Lugares disponibles:")
    print(calcular_lugares_disponibles(unidades))

    print("\nUnidades llenas:")
    print(mostrar_unidades_llenas(unidades))

    print("\nUnidad con mayor ocupación:")
    print(unidad_mayor_ocupacion(unidades).__dict__)

if __name__ == "__main__":
    main()
