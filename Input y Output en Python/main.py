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