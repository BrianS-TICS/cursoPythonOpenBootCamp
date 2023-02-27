class Nodo:
    
    dato = 0
    izquierda = 0
    derecha = 0

    def __init__(self, dato):
        self.dato = dato  # Cabeza
        self.izquierda = None
        self.derecha = None
