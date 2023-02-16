class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return ("color: " + self.color, " ruedas: " + self.ruedas + " puertas: " + self.puertas)


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self) :
        return super(Coche, self).__str__() + " velocidad : " + f'{self.velocidad}' + "  cilindrada : " + f'{self.cilindrada}'

nissan=Coche('Negro', 4, 4, 255, 8)
print(nissan.__str__())
