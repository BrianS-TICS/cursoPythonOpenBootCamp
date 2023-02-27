
Arbol = {
    "1": ['2', '3'],
    "2": ['4', '5'],
    "3": ['6', '7'],
    "4": ['8', '9'],
    "5": ['10', '11'],
    "6": ['12', '13'],
    "7": ['14', '15'],
    "8": ['16', '17'],
    "9": ['18', '19'],
    "10": ['20', '21'],
    "11": ['22', '23'],
    "12": ['24', '25'],
}

estadoInicial = '1'
meta = '11'
frontera = [estadoInicial]


def B_A(frontera):
    
    estadoActual = frontera.pop(0)
    if estadoActual == meta:
        print('Encontrado')
        return True
    else:
        os = Arbol[estadoActual]
        frontera.extend(os)
        B_A(frontera)


resultado = B_A(frontera)

