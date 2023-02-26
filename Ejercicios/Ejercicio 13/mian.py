from functools import reduce

lista = [1, 2, 4, 5, 6, 7, 8, 2, 1]


def condition(item):
    if item % 2 != 0:
        return True
    return False


def main():
    listaDeImpares = list(filter(condition, lista))
    print(listaDeImpares)
    sumaDeDatos = reduce(lambda acum, current: acum + current, listaDeImpares)
    print("Suma de numeros impares")
    print(sumaDeDatos)


if __name__ == '__main__':
    main()
    pass
