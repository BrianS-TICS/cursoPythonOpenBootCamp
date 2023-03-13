import sys
def es_seguro(tablero, fila, columna):
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


def resolver_n_reinas(n):
    """
    Función para resolver el problema de las N reinas.
    """
    tablero = [-1] * n

    def resolver_reinas_util(columna):
        # Si todas las reinas se han colocado, se ha encontrado una solución
        if columna == n:
            print(tablero)
            sys.exit()
            return True

        # Probar a colocar una reina en cada fila de la columna actual
        for fila in range(n):
            if es_seguro(tablero, fila, columna):
                tablero[columna] = fila

                # Continuar con la siguiente columna
                resolver_reinas_util(columna + 1)

        # Reiniciar la columna actual
        tablero[columna] = -1

    # Llamar a la función auxiliar para resolver el problema
    resolver_reinas_util(0)


# Ejemplo de uso: resolver el problema de las 8 reinas
resolver_n_reinas(50)