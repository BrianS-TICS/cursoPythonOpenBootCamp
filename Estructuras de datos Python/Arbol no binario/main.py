def expand(nodo):
    hijos = []

    if (nodo.children != [] or nodo.children != None):
        hijos = nodo.children
        return hijos

    return hijos


# class Nodo:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

#     def add_child(self, node):
#         self.children.append(node)
        
def valida(tablero, fila, columna):
    """
    Función auxiliar para verificar si es seguro colocar una reina en la fila y columna especificadas.
    """
    # Verificar la fila
    for i in range(columna):
        if tablero[i] == fila:
            return False
        # Verificar diagonal superior izquierda
        if tablero[i] - i == fila - columna:
            return False
        # Verificar diagonal inferior izquierda
        if tablero[i] + i == fila + columna:
            return False

    # Es seguro colocar una reina en la fila y columna especificadas
    return True

def intentaColocar(tablero, numero, columna):
    # Probar a colocar una reina en cada fila de la columna actual
    for fila in range(numero):
        if valida(tablero, fila, columna):
            tablero[columna] = fila

            # Continuar con la siguiente columna
            intentaColocar(columna + 1)


def defineTablero(numero):
    tablero = [0] * numero
    intentaColocar(tablero, numero, columna=0)




def busqueda_ancho(f):
    if len(f) == 0:
        print('No existe')
        return False
    else:
        estado_actual = f.pop(0)
        print(estado_actual.valor)
        if estado_actual.valor == meta:
            print('Encontrado')
            return True
        else:
            os = expand(estado_actual)
            f.extend(os)
    busqueda_ancho(f)


inicial = Nodo("A")
