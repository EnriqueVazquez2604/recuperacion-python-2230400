import pytest

from examen_recuperacion_2230400.models import Unidad
from examen_recuperacion_2230400.services import (
    buscar_unidad,
    calcular_lugares_disponibles,
    mostrar_unidades_llenas,
    registrar_unidad,
    resumen_general,
    unidad_mayor_ocupacion,
)


def test_registrar_unidad_exitosa():
    unidades = []
    u = Unidad(1, "Carlos", 20, 18, "Ruta Norte")
    registrar_unidad(unidades, u)
    assert len(unidades) == 1


def test_registrar_unidad_duplicada():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    with pytest.raises(ValueError):
        registrar_unidad(unidades, Unidad(1, "Ana", 15, 10, "Ruta Sur"))


def test_buscar_unidad_existente():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    resultado = buscar_unidad(unidades, 1)
    assert resultado is not None


def test_buscar_unidad_inexistente():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    resultado = buscar_unidad(unidades, 99)
    assert resultado is None


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


def test_resumen_general():
    unidades = [
        Unidad(1, "Carlos", 20, 18, "Ruta Norte"),
        Unidad(2, "Ana", 15, 15, "Ruta Sur"),
    ]
    resumen = resumen_general(unidades)
    assert resumen["total_unidades"] == 2
