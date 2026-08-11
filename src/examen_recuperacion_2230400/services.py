def calcular_lugares_disponibles(unidades):
    return [
        {"numero": u.numero, "disponibles": u.capacidad - u.pasajeros}
        for u in unidades
    ]

def mostrar_unidades_llenas(unidades):
    return [u for u in unidades if u.pasajeros >= u.capacidad]

def unidad_mayor_ocupacion(unidades):
    return max(unidades, key=lambda u: u.pasajeros, default=None)
