from modulos.recoleccion import recolectar_residuos
from modulos.almacenamiento import Almacen

def main():
    almacen = Almacen()
    total_dias = 10  # Ejemplo de 10 días

    for dia in range(1, total_dias + 1):
        residuos = recolectar_residuos(dia)
        almacen.zona_llegada.extend(residuos)
        
        # Transferir residuos al almacén cada tercer día
        almacen.mover_a_almacen(dia)

        # Salida de información diaria
        print(f"Día {dia}:")
        print("Zona de Llegada:", [f"{r.tipo} desde {r.origen}" for r in almacen.zona_llegada])
        print("Zona de Almacén:", [f"{r.tipo} desde {r.origen}" for r in almacen.zona_almacen])
        print("-----")

if __name__ == "__main__":
    main()
