# Formateo de cadenas

texto = "numero"
numero = 5
numeroDiferente = 10.2
# Formas legacy
print("Legacy mostrar por '%' usando tuplas")
print("Esto imprime un %s %d %.2f" % (texto, numero, numeroDiferente))

# Formas actuales
print("Usando metodo de cadena .format")
print("Esto es un {} y el valor es {} este es otro {}".format(
    numero, texto, numeroDiferente))
# Invirtiendo los valores de indexacion
print("Esto es un {2} y el valor es {1} este es otro {0}".format(
    numero, texto, numeroDiferente))
# Usando parametros nombrados
print("Esto es un {a} y el valor es {b} este es otro {c}".format(
    a=numero, b=texto, c=numeroDiferente))

print("Usando metodo de cadena f'string'")
print(f'El {texto.upper()} es {numero} y uno diferente es {numeroDiferente}')

# Convertir a strings
n = 100
ntext = str(n)
print(type(n))
print(type(ntext))

# Representacion de __str__ y __repr__


class Auto:
    velocidad = 0
    modelo = ""

    def __init__(self, modelo, velocidad):
        self.modelo = modelo
        self.velocidad = velocidad

    # __str__ para salidas informales
    def __str__(self) -> str:
        return f'El modelo es {self.modelo}, la velocidad es {self.velocidad}'

    # __repr__ para salidas tecnicas de desarrollo o depuracion
    def __repr__(self) -> str:
        return f'{self.modelo}, {self.velocidad}'


auto = Auto("Altima", 220)
print(str(auto))
print(repr(auto))

# Funciones decadenas
cadena = "  Almacenamiento de caracteres  "

print(cadena.capitalize())
print(cadena.upper())
print(cadena.title())
print(cadena.lower())
print(cadena.count("a"))
print(cadena.lower().count("a"))
# Valida por valores solo alfanumericos
print(cadena.isalnum())
# Elimina espacios iniciales y finales
print(cadena.strip())
# Elimina espacios iniciales y finales
print(cadena.split('de'))
# Valida por existencia de caracteres
print(cadena.startswith('Almacenamiento'))
