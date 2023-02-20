import pickle
def main():
    vehiculo = Vehiculo('Camaro', 220)
    f = open('vehiculo.bin', 'wb')
    pickle.dump(vehiculo, f)
    
    f = open('vehiculo.bin', 'rb')
    datosRecuperados= pickle.load(f)
    print(datosRecuperados)

pass


class Vehiculo:
    nombre = ''
    velocidad = 0

    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad

    def __str__(self) -> str:
        return f'{self.nombre}, {self.velocidad}'

if (__name__ == "__main__"):
    main()
