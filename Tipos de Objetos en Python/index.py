# MUTABILIDAD
# ? 1.1 Cuando mutamos una variable no reescribimos un elementento en el mismo espacio de memtorio, reservamos uno nuevo y despues el interprete se encarga de liberar el anterior
# ! Un ejemplo de estructura mutable es una lista
# ! | Sintaxis | Tupla es tupla = () | Lista es lista = []
# ? 1.2 La diferencia entre una tupla y una lista es que una lista, una vez definida se puede alterar una tupla no

# ? Prueba de seccion 1.2
lista = ['a', 'b', 'c']
lista[0] = 'P'
lista.append('S')
lista.append('B')
lista.append('A')
lista.remove('A')
print(lista)

listaVocales = ['a', 'e', 'i', 'o', 'u']
listaBad = ['n', 'i', 'g', 'j', 'a']
listaVocales.append(listaBad)  # * Crea lista anidada
print(listaVocales)

# ! SIMILAR A JSONS
# DICCIONARIOS
diccionario = {
    "name": "rodolfo",
    "age": 22,
    "created_at": "2020/02/01"
}

print(diccionario)
print(diccionario["name"])
diccionario["name"] = "Jose"
print(diccionario["name"])

# ? Existen dos maneras de eliminar elementos de un diccionario
# ? diccionario.del() y diccionario.pop()
# ? La diferencia es que pop retorna el valor del elemento eliminado y del no retorna nada

# CONJUNTOS
# ? Los conjuntos no pueden tener valores duplicados eso los diferencia con una lista
conjunto = {1, 2, 3, 4, 5}
conjuntoExtra = {9, 494, 254}

# Operaciones con conjuntos
# ! operador | para union
print(conjunto | conjuntoExtra)

# ! operador & para interseccion
print(conjunto & conjuntoExtra)

# ! operador - para diferencia
print(conjunto - conjuntoExtra)

# ! operador ^ para diferencia simetrica ( valores diferentes despues de la union que no se repiten)
print(conjunto ^ conjuntoExtra)

# Eliminar elemento de diccionario por clave
diccionario.pop("name")
print(diccionario)

# INMUTABILIDAD

a = 5
# * Imprime el tipo de dato
print(type(a))

# * Imprime la direccion de memoria en donde esta el valor de la variable
print(id(a))  # ? Si al ejecutar python no hay una variable que apunte a la direccion de memoria será eliminada

# ? Prueba de la seccion 1.1
a = 10
print(id(a))

# ! Tupla => Lista ordenada de elementos finitos. { + - ( arrys inmutables ) }
# ! Por lo tanto los numeros, cadenas y tuplas en python son inmutables
# ! Tambien es un lenguaje dinamico -> Permitiendo cambiar el tipo de estructura de dato de una misma variable según se desee.

##################################################################################

# ? Metodos de cadenas
texto = "mi texto"
print(texto.capitalize())
print(texto.title())
print(texto.lower())
print(texto.upper())
print(texto.replace('i', 'e'))
print(texto.find('es'))  # ! Retorna posicion del valor o -1 si no existe
print(texto.find('texto'))

# ! Convierte palabras de una cadena en elementos de un arreglo en funcion a los espacios de esta
print(texto.split())
# ! Es posible dar un parametro para separar los elementos segun la existencia del paramentro
print(texto.split('t'))

listaCadenas = ['Solamente', 'una', 'palabra', 'y', 'media']

# ! Join inserta los datos en un string tomando como parametro un elemento que sera usando para separar los datos insertados
print(' '.join(listaCadenas))

# OPERADORES

# Operador de asignacion
variable = 2
variable+= 5
variable-= 5
variable*= 5
variable/= 5
variable**= 5



# Operadores aritmeticos
suma = 1 + 1
multiplicar = 20 * 32
resto = 10 % 10  # * El resto de la operacion de divicion entre 10 y 10
resto = 10 // 10  # * El resultado de la divicion entre 10 y 10

potenciacion = 8 ** 8 # * Potencia de un numero
