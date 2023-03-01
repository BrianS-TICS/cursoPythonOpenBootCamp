
def expand(nodo):
    hijos = []

    if nodo.izquierda:
        hijos.append(nodo.izquierda)
    if nodo.derecha:
        hijos.append(nodo.derecha)

    return hijos


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self, valor):
        self.raiz = Nodo(valor)

    def insertarAncho(self, valor, stack=[]):
        if not stack:
            stack = [self.raiz]

        if not stack:
            return

        else:
            nodo = stack.pop(0)

            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
                return
            elif nodo.derecha is None:
                nodo.derecha = Nodo(valor)
                return
            else:
                hijos = expand(nodo)
                stack.extend(hijos)

        self.insertarAncho(valor, stack)


arbol = ArbolBinario(1)
arbol.insertarAncho(2)
arbol.insertarAncho(3)
arbol.insertarAncho(4)
arbol.insertarAncho(5)
arbol.insertarAncho(6)
arbol.insertarAncho(7)
arbol.insertarAncho(8)


def busqueda_largo(f):
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
            f = os + f
    busqueda_largo(f)


meta = 8
frontera = [arbol.raiz]
busqueda_largo(frontera)
