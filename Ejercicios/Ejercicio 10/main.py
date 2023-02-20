def main():
    nombreFichero = 'Exercise10.txt'
    contenidoFichero = ["Este sera un ejemplo\n", 'de dos lineas']
    creation(nombreFichero)
    escribir(nombreFichero, contenidoFichero)


def creation(nombreFichero):
    f = open(nombreFichero, 'xt')
    f.close()


def escribir(nombreFichero, contenido):
    f = open(nombreFichero, 'a')
    f.writelines(contenido)
    f.close()


if (__name__ == "__main__"):
    main()
