class Almacen:
    def __init__(self):
        self.zona_llegada = []
        self.zona_almacen = []

    def mover_a_almacen(self, dia):
        if dia % 3 == 0:
            self.zona_almacen.extend(self.zona_llegada)
            self.zona_llegada = []
