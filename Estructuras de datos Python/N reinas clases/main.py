def busqueda_ancho(frontera):

    pass


def colocarReina(fila, vector, longitud, ataques):

    if fila == longitud:
        print(vector)
        return 1
    else:
        # Calcula ataques
        for i in range(longitud):
            for j in range(i+1, longitud):
                if vector[i] == vector[j]:
                    ataques += 2
                if abs(i - j) == abs(vector[i] - vector[j]):
                    ataques += 2
    


def inicioVector(longitud):
    vector = [0]*longitud
    print(vector)

    fila = 0
    ataques = 0

    # Goal test
    # arrayAtaques = ataques
    # if ataques == 0:
    #     return True
    # else:
    #     return False

    return colocarReina(fila, vector, longitud, ataques)


inicioVector(4)
