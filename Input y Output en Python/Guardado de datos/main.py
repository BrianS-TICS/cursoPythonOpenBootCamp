# Guardado de ficheros

# a = permiso de adjuntacion
# r = permiso de lectura
# w = permiso de escritura
# x = creacion

# t = texto
# b = binary

def main():
    
    lineas = ["La casa esta limpia\n", "Solo tienes que sacudir"]
    escribe('C:/Users/brian/Desktop/PYTHON_OPENBOOTCAMP/Input y Output en Python/Guardado de datos/ficheroGenerado.txt', lineas)
    # obtenerElementosDeFicheros()
    
    # def obtenerElementosDeFicheros():
    #     listaDePalabras = [
    #         "Linea numero 1\n",
    #         "Linea numero 2\n",
    #         "Linea numero 3\n"
    #     ]

    #     f = open(
    #         'C:/Users/brian/Desktop/PYTHON_OPENBOOTCAMP/Input y Output en Python/Guardado de datos/datos.txt', 'w')
    #     f.writelines(listaDePalabras)

    # datos = f.readlines()
    # print(datos)
    # f.close()

    # for linea in datos:
    #     print(linea)
    pass

def escribe(rutaAndNombre, lineas) : 
    f =  open(rutaAndNombre, 'w')
    f.writelines(lineas)
    
    pass

if (__name__ == "__main__"):
    main()
