import pickle

def main() :
    print("Funcionando")
    juguete = Jueguete("Caballo de madera", 900)
    # Guardado de datos binarios
    # f = open('dump.bin', 'wb')
    # pickle.dump(juguete, f)
    # f.close()

    # Lectura de datos en binario
    f = open('dump.bin', 'rb')
    datosRecuperados = pickle.load(f)
    print(datosRecuperados)
    
class Jueguete : 
    nombre = ""
    precio = 0
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def getNombre(self) :
        return self.nombre

    def __str__(self) -> str:
        return f'{self.nombre} tiene un precio de {self.precio}'
        pass

if (__name__ == "__main__") :
    main()