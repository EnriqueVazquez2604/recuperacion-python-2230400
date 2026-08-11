from .models import Unidad
from .services import registrar_unidad


def main():
    unidades = []

    unidad1 = Unidad(1, "Carlos", 40, 25, "Ruta Norte")

    resultado = registrar_unidad(unidades, unidad1)

    print(resultado)
    print(unidades)