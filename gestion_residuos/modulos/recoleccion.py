from modelos.residuo import Residuo
from config.configuracion import Config

def recolectar_residuos(dia):
    residuos_dia = []
    
    if dia in Config.OFICINA["dias"]:
        residuos_dia.append(Residuo("biodegradables", Config.OFICINA["sede"]))
    
    if (dia % 2 == 1) and Config.PRINCIPAL["dias"] == "impar":
        residuos_dia.append(Residuo("plasticos", Config.PRINCIPAL["sede"]))
    
    if (dia % 2 == 0) and Config.SECUNDARIA["dias"] == "par":
        residuos_dia.append(Residuo("peligrosos", Config.SECUNDARIA["sede"]))
    
    return residuos_dia
