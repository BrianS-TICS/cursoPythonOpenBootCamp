# Calculadora de indice de masa corporal
import decimal

altura = float(input("Escribe tu altura "))
peso = float(input("Escribe tu peso "))


def calculaIMC(altura, peso):
    alturaCuadrada = altura * altura
    imc = decimal.Decimal(alturaCuadrada // peso)
    rounded = imc.quantize(decimal.Decimal('0.00'))
    return rounded


imc = calculaIMC(altura, peso)

print(f"Tu IMC es de {imc} ")
