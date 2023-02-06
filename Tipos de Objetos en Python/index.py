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
