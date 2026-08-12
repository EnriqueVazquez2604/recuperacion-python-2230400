def validar_unidad(unidad):
    if unidad.capacidad <= 0:
        raise ValueError("La capacidad debe ser mayor que cero.")
    if unidad.pasajeros < 0:
        raise ValueError("Los pasajeros no pueden ser negativos.")
    if unidad.pasajeros > unidad.capacidad:
        raise ValueError("Pasajeros no pueden exceder la capacidad.")


def registrar_unidad(unidades, unidad):
    if any(u.numero == unidad.numero for u in unidades):
        raise ValueError("Número de unidad duplicado.")
    validar_unidad(unidad)
    unidades.append(unidad)


def mostrar_unidades(unidades):
    return unidades


def buscar_unidad(unidades, numero):
    for unidad in unidades:
        if unidad.numero == numero:
            return unidad
    return None


def actualizar_unidad(unidades, numero, nuevos_datos):
    unidad = buscar_unidad(unidades, numero)
    if unidad is None:
        raise ValueError("Unidad no encontrada.")

    campos_permitidos = {"conductor", "capacidad", "pasajeros", "ruta"}
    if set(nuevos_datos) - campos_permitidos:
        raise ValueError("Campo de actualización no permitido.")

    valores = {
        "conductor": unidad.conductor,
        "capacidad": unidad.capacidad,
        "pasajeros": unidad.pasajeros,
        "ruta": unidad.ruta,
    }
    valores.update(nuevos_datos)

    if valores["capacidad"] <= 0:
        raise ValueError("La capacidad debe ser mayor que cero.")
    if valores["pasajeros"] < 0:
        raise ValueError("Los pasajeros no pueden ser negativos.")
    if valores["pasajeros"] > valores["capacidad"]:
        raise ValueError("Pasajeros no pueden exceder la capacidad.")

    for clave, valor in nuevos_datos.items():
        setattr(unidad, clave, valor)


def eliminar_unidad(unidades, numero):
    unidad = buscar_unidad(unidades, numero)
    if unidad is None:
        raise ValueError("Unidad no encontrada.")
    unidades.remove(unidad)


def calcular_lugares_disponibles(unidades):
    return [
        {"numero": unidad.numero, "disponibles": unidad.capacidad - unidad.pasajeros}
        for unidad in unidades
    ]


def mostrar_unidades_llenas(unidades):
    return [unidad for unidad in unidades if unidad.pasajeros >= unidad.capacidad]


def unidad_mayor_ocupacion(unidades):
    return max(unidades, key=lambda unidad: unidad.pasajeros, default=None)


def resumen_general(unidades):
    total = len(unidades)
    promedio = sum(u.pasajeros for u in unidades) / total if total else 0
    return {"total_unidades": total, "promedio_ocupacion": promedio}
