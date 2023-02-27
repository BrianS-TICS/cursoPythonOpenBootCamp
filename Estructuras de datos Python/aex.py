arbolBinario = [1, [2, [], []], [3, [], []]]

estadoInicial = 1
meta = 3
frontera = [estadoInicial]


def B_A(frontera):
    estadoActual = frontera.pop(0)
    print(meta)
    
    if estadoActual == meta:
        return True
    
    else:
        os = arbolBinario[estadoActual]
        frontera.extend(os)

        B_A(frontera)

B_A(arbolBinario)