# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def checkIfIsBisiento(year):
    result = False
    if (year % 4 == 0):
        result = True
    return result


year = float(input("Escribe el año "))
isBisiesto = checkIfIsBisiento(year)
if (isBisiesto):
    print("El año es biciesto")
else:
    print("El año no es biciesto")
