from examen_recuperacion_2230400.models import Unidad
from examen_recuperacion_2230400.services import (
    calcular_lugares_disponibles,
    mostrar_unidades_llenas,
    unidad_mayor_ocupacion,
)

def test_calcular_lugares_disponibles():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    resultado = calcular_lugares_disponibles(unidades)
    assert resultado[0]["disponibles"] == 2

def test_mostrar_unidades_llenas():
    unidades = [Unidad(1, "Ana", 15, 15, "Ruta Sur")]
    llenas = mostrar_unidades_llenas(unidades)
    assert len(llenas) == 1

def test_unidad_mayor_ocupacion():
    unidades = [
        Unidad(1, "Carlos", 20, 18, "Ruta Norte"),
        Unidad(2, "Ana", 15, 15, "Ruta Sur"),
    ]
    mayor = unidad_mayor_ocupacion(unidades)
    assert mayor.numero == 1
