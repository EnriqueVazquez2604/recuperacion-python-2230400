class Unidad:
    def __init__(self, numero, conductor, capacidad, pasajeros, ruta):
        self.numero = numero
        self.conductor = conductor
        self.capacidad = capacidad
        self.pasajeros = pasajeros
        self.ruta = ruta

    def __repr__(self):
        return f"Unidad({self.numero}, {self.conductor}, {self.capacidad}, {self.pasajeros}, {self.ruta})"
