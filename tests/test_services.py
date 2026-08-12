import pytest

from examen_recuperacion_2230400.models import Unidad
from examen_recuperacion_2230400.services import (
    actualizar_unidad,
    buscar_unidad,
    calcular_lugares_disponibles,
    eliminar_unidad,
    mostrar_unidades_llenas,
    registrar_unidad,
    resumen_general,
    unidad_mayor_ocupacion,
)


def test_registrar_unidad_exitosa():
    unidades = []
    unidad = Unidad(1, "Carlos", 20, 18, "Ruta Norte")
    registrar_unidad(unidades, unidad)
    assert len(unidades) == 1
    assert unidades[0] is unidad


def test_registrar_unidad_duplicada():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    with pytest.raises(ValueError, match="duplicado"):
        registrar_unidad(unidades, Unidad(1, "Ana", 15, 10, "Ruta Sur"))


def test_buscar_unidad_existente():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    assert buscar_unidad(unidades, 1) is unidades[0]


def test_buscar_unidad_inexistente():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    assert buscar_unidad(unidades, 99) is None


def test_calcular_lugares_disponibles():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    assert calcular_lugares_disponibles(unidades) == [
        {"numero": 1, "disponibles": 2}
    ]


def test_mostrar_unidades_llenas():
    unidades = [
        Unidad(1, "Ana", 15, 15, "Ruta Sur"),
        Unidad(2, "Luis", 20, 10, "Ruta Centro"),
    ]
    llenas = mostrar_unidades_llenas(unidades)
    assert len(llenas) == 1
    assert llenas[0].numero == 1


def test_unidad_mayor_ocupacion():
    unidades = [
        Unidad(1, "Carlos", 20, 18, "Ruta Norte"),
        Unidad(2, "Ana", 15, 15, "Ruta Sur"),
    ]
    assert unidad_mayor_ocupacion(unidades).numero == 1


def test_resumen_general():
    unidades = [
        Unidad(1, "Carlos", 20, 18, "Ruta Norte"),
        Unidad(2, "Ana", 15, 15, "Ruta Sur"),
    ]
    resumen = resumen_general(unidades)
    assert resumen["total_unidades"] == 2
    assert resumen["promedio_ocupacion"] == 16.5


def test_registrar_unidad_capacidad_invalida():
    with pytest.raises(ValueError, match="capacidad"):
        registrar_unidad([], Unidad(1, "Carlos", 0, 0, "Ruta Norte"))


def test_registrar_unidad_pasajeros_negativos():
    with pytest.raises(ValueError, match="negativos"):
        registrar_unidad([], Unidad(2, "Ana", 20, -5, "Ruta Sur"))


def test_registrar_unidad_pasajeros_exceden_capacidad():
    with pytest.raises(ValueError, match="exceder"):
        registrar_unidad([], Unidad(3, "Luis", 10, 15, "Ruta Centro"))


def test_actualizar_unidad():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    actualizar_unidad(unidades, 1, {"conductor": "Pedro", "pasajeros": 12})
    assert unidades[0].conductor == "Pedro"
    assert unidades[0].pasajeros == 12


def test_actualizar_unidad_con_datos_invalidos():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    with pytest.raises(ValueError, match="exceder"):
        actualizar_unidad(unidades, 1, {"pasajeros": 25})
    assert unidades[0].pasajeros == 18


def test_eliminar_unidad():
    unidades = [Unidad(1, "Carlos", 20, 18, "Ruta Norte")]
    eliminar_unidad(unidades, 1)
    assert unidades == []
