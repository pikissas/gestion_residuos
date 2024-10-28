from config.configuracion import Config

class Residuo:
    def __init__(self, tipo, origen):
        self.tipo = tipo
        self.color = Config.TIPOS_RESIDUOS[tipo]
        self.origen = origen
