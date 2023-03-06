
def esValido(fila, columna, reinas):
    for f in range(fila):
        # reinas[f] === Columnas en donde ya colocamos alguna dama
        if columna == reinas[f]:
            return False
        elif abs(columna - reinas[f]) == abs(fila - f):
            return False
    return True


def colocaReina(fila, reinas, size):

    if fila == size:
        print(reinas)
        return 1
    else:
        totalSoluciones = 0
        for columa in range(size):
            if esValido(fila, columa, reinas):
                reinas[fila] = columa
                totalSoluciones += colocaReina(fila+1, reinas, size)
        return totalSoluciones


def numeroReinas(size):
    reinas = [0]*size
    fila = 0
    return colocaReina(fila, reinas, size)


numeroReinas(6)
