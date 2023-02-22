from functools import reduce
from getpass import getpass
numeros = [1, 2, 3, 4, 5, 6]

# ===== Filter =====


def filtro(x):
    if (x % 2 == 0):
        return True
    return False


resultado = filter(filtro, numeros)
print(list(resultado))

# lamda = funcion anonima


def cuadrado(x):
    return x * x


# ===== Map =====
resultadoMap = map(cuadrado, numeros)
print(list(resultadoMap))


def validaDivisibles(x, y):
    return x + y


print(numeros)
arrayReducido = reduce(validaDivisibles, numeros)
print(arrayReducido)

# ===== Zip =====
# Asocia 2 listas en una sola tupla
cursos = ["Java", "Git", "Python"]
asistentes = [15, 20, 4]
demo = zip(cursos, asistentes)
print(list(demo))


# ===== Zip =====
# Valida por la veracidad de un solo elemento de una condicion en una lista y retorna boleano
lista = [1 == 1, 2 == 2, 3 == 1]
resAny = any(lista)
# Valida por la veracidad de todos los elementos de una condicion en una lista y retorna boleano
resAll = all(lista)
print(resAny)
print(resAll)

a = 1.444
print(round(a))

# min devuelve el valor mas bajo de una lista
print(min([1, 5, 6, 7, 8]))

# pow devuelve el valor elevado a un exponente
print(pow(2,5))

# sorted ordena una lista
print(sorted(["a", "s" , "x", "b"], reverse=True))

a = input("Como te llamas ")
print(f"Hola, {a}")

p = getpass("EScribe tu password ")
print(f"Este es {p}")

# Digito a string
secreto = 50
tecleado = input("Introduce un numero")
valor = int(tecleado)
print(valor)