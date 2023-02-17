from pprint import pprint

class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

nissan=Coche('Negro', 4, 4, 255, 8)

pprint(vars(nissan))