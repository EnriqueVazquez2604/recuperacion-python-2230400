def registrar_unidad(unidades, unidad):
    if any(u.numero == unidad.numero for u in unidades):
        raise ValueError("Número de unidad duplicado.")
    if unidad.pasajeros > unidad.capacidad:
        raise ValueError("Pasajeros no pueden exceder la capacidad.")
    unidades.append(unidad)


def mostrar_unidades(unidades):
    return unidades


def buscar_unidad(unidades, numero):
    for u in unidades:
        if u.numero == numero:
            return u
    return None


def actualizar_unidad(unidades, numero, nuevos_datos):
    unidad = buscar_unidad(unidades, numero)
    if unidad is None:
        raise ValueError("Unidad no encontrada.")
    for clave, valor in nuevos_datos.items():
        setattr(unidad, clave, valor)


def eliminar_unidad(unidades, numero):
    unidad = buscar_unidad(unidades, numero)
    if unidad:
        unidades.remove(unidad)
    else:
        raise ValueError("Unidad no encontrada.")


def calcular_lugares_disponibles(unidades):
    return [
        {"numero": u.numero, "disponibles": u.capacidad - u.pasajeros} for u in unidades
    ]


def mostrar_unidades_llenas(unidades):
    return [u for u in unidades if u.pasajeros >= u.capacidad]


def unidad_mayor_ocupacion(unidades):
    return max(unidades, key=lambda u: u.pasajeros, default=None)


def resumen_general(unidades):
    total = len(unidades)
    promedio_ocupacion = sum(u.pasajeros for u in unidades) / total if total > 0 else 0
    return {"total_unidades": total, "promedio_ocupacion": promedio_ocupacion}
