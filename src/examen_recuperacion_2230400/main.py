from examen_recuperacion_2230400.models import Unidad
from examen_recuperacion_2230400.services import (
    actualizar_unidad,
    buscar_unidad,
    calcular_lugares_disponibles,
    eliminar_unidad,
    mostrar_unidades,
    mostrar_unidades_llenas,
    registrar_unidad,
    resumen_general,
    unidad_mayor_ocupacion,
)


def mostrar_unidad(unidad):
    return (
        f"Unidad {unidad.numero} | Conductor: {unidad.conductor} | "
        f"Capacidad: {unidad.capacidad} | Pasajeros: {unidad.pasajeros} | "
        f"Ruta: {unidad.ruta}"
    )


def pedir_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Introduce un número entero.")


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El texto no puede estar vacío.")


def registrar_desde_menu(unidades):
    print("\n=== Registrar unidad ===")
    numero = pedir_entero("Número de unidad: ", 1)
    conductor = pedir_texto("Conductor: ")
    capacidad = pedir_entero("Capacidad: ", 1)
    pasajeros = pedir_entero("Pasajeros: ", 0)
    if pasajeros > capacidad:
        print("Los pasajeros no pueden exceder la capacidad.")
        return
    ruta = pedir_texto("Ruta: ")
    try:
        registrar_unidad(unidades, Unidad(numero, conductor, capacidad, pasajeros, ruta))
        print("Unidad registrada correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def mostrar_todas(unidades):
    print("\n=== Todas las unidades ===")
    if not unidades:
        print("No hay unidades registradas.")
        return
    for unidad in mostrar_unidades(unidades):
        print(mostrar_unidad(unidad))


def buscar_desde_menu(unidades):
    print("\n=== Buscar unidad ===")
    numero = pedir_entero("Número de unidad: ", 1)
    unidad = buscar_unidad(unidades, numero)
    if unidad is None:
        print("No se encontró una unidad con ese número.")
    else:
        print(mostrar_unidad(unidad))


def actualizar_desde_menu(unidades):
    print("\n=== Actualizar unidad ===")
    numero = pedir_entero("Número de unidad: ", 1)
    unidad = buscar_unidad(unidades, numero)
    if unidad is None:
        print("No se encontró una unidad con ese número.")
        return

    print("Deja el campo vacío para conservar el valor actual.")
    conductor = input(f"Conductor [{unidad.conductor}]: ").strip()
    capacidad_texto = input(f"Capacidad [{unidad.capacidad}]: ").strip()
    pasajeros_texto = input(f"Pasajeros [{unidad.pasajeros}]: ").strip()
    ruta = input(f"Ruta [{unidad.ruta}]: ").strip()
    datos = {}
    if conductor:
        datos["conductor"] = conductor
    if capacidad_texto:
        try:
            datos["capacidad"] = int(capacidad_texto)
        except ValueError:
            print("La capacidad debe ser un número entero.")
            return
    if pasajeros_texto:
        try:
            datos["pasajeros"] = int(pasajeros_texto)
        except ValueError:
            print("Los pasajeros deben ser un número entero.")
            return
    if ruta:
        datos["ruta"] = ruta
    try:
        actualizar_unidad(unidades, numero, datos)
        print("Unidad actualizada correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def eliminar_desde_menu(unidades):
    print("\n=== Eliminar unidad ===")
    numero = pedir_entero("Número de unidad: ", 1)
    try:
        eliminar_unidad(unidades, numero)
        print("Unidad eliminada correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def mostrar_lugares_disponibles(unidades):
    print("\n=== Lugares disponibles ===")
    if not unidades:
        print("No hay unidades registradas.")
        return
    for dato in calcular_lugares_disponibles(unidades):
        print(f"Unidad {dato['numero']} -> {dato['disponibles']} lugares disponibles")


def mostrar_llenas(unidades):
    print("\n=== Unidades llenas ===")
    llenas = mostrar_unidades_llenas(unidades)
    if not llenas:
        print("No hay unidades llenas.")
        return
    for unidad in llenas:
        print(mostrar_unidad(unidad))


def mostrar_mayor_ocupacion(unidades):
    print("\n=== Unidad con mayor ocupación ===")
    mayor = unidad_mayor_ocupacion(unidades)
    if mayor is None:
        print("No hay unidades registradas.")
    else:
        print(mostrar_unidad(mayor))


def mostrar_resumen(unidades):
    print("\n=== Resumen general ===")
    resumen = resumen_general(unidades)
    print(f"Total de unidades: {resumen['total_unidades']}")
    print(f"Promedio de ocupación: {resumen['promedio_ocupacion']:.2f} pasajeros")


def mostrar_menu():
    print(
        """
=== CONTROL DE TRANSPORTE ESCOLAR ===
1. Registrar unidad
2. Mostrar unidades
3. Buscar unidad
4. Actualizar unidad
5. Eliminar unidad
6. Mostrar lugares disponibles
7. Mostrar unidades llenas
8. Mostrar unidad con mayor ocupación
9. Mostrar resumen general
0. Salir
"""
    )


def main():
    unidades = [
        Unidad(1, "Carlos", 20, 18, "Ruta Norte"),
        Unidad(2, "Ana", 15, 15, "Ruta Sur"),
        Unidad(3, "Luis", 25, 10, "Ruta Centro"),
    ]
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            registrar_desde_menu(unidades)
        elif opcion == "2":
            mostrar_todas(unidades)
        elif opcion == "3":
            buscar_desde_menu(unidades)
        elif opcion == "4":
            actualizar_desde_menu(unidades)
        elif opcion == "5":
            eliminar_desde_menu(unidades)
        elif opcion == "6":
            mostrar_lugares_disponibles(unidades)
        elif opcion == "7":
            mostrar_llenas(unidades)
        elif opcion == "8":
            mostrar_mayor_ocupacion(unidades)
        elif opcion == "9":
            mostrar_resumen(unidades)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Selecciona una opción del 0 al 9.")


if __name__ == "__main__":
    main()
