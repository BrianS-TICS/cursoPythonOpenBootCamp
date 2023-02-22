numeros = [1, 2, 3, 4, 5, 6]

def filtro (x) :
    if(x % 2 == 0) : 
        return True
    return False
    
resultado = filter(filtro, numeros)
print(list(resultado))

# lamda = funcion anonima

def cuadrado(x) : 
    return x * x

resultadoMap = map(cuadrado, numeros)
print(list(resultadoMap))