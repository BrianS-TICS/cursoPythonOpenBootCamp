
class Nodo:

    def __init__(self, dato):
        self.dato = dato  # Cabeza
        self.izquierda = None
        self.derecha = None

    def agrega(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquieda = Nodo(dato)
            else:
                self.agrega(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.agrega(nodo.derecha, dato)

    def preorden(self , nodo) :
        if nodo is not None :
            print(f'{nodo.dato}', end=" => " )
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

# Se inicia con cabeza
nodo = Nodo(1)
nodo.agrega(nodo, 2)
nodo.agrega(nodo, 3)
nodo.agrega(nodo, 4)
nodo.agrega(nodo, 5)
nodo.agrega(nodo, 6)
nodo.agrega(nodo, 7)
nodo.agrega(nodo, 8)
nodo.agrega(nodo, 9)
nodo.agrega(nodo, 10)
nodo.agrega(nodo, 11)
nodo.agrega(nodo, 12)
nodo.agrega(nodo, 13)
nodo.agrega(nodo, 14)
nodo.agrega(nodo, 15)
nodo.preorden(nodo)

