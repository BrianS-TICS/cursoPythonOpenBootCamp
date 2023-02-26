import pprint
def main():
    print("Escribe un lista de paises")
    datosObtenidos = input()
    lista = datosObtenidos.split(', ')
    print(lista)

    paisesUnicos = sorted(list(set(lista)))
    
    print("Lista de paises ordenados y no repetidos")
    pprint.pprint(paisesUnicos)


if __name__ == '__main__':
    main()
    pass
