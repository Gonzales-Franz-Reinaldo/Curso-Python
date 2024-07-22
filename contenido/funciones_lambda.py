multiplo = lambda x : x * 2

print('El resultado es: ', multiplo(2))

numeros = [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16]

# funcion comun para verificar los numeros pares 
def is_par(num):
    if(num % 2 == 0):
        return True
    
# usando filter en una función común
numeros_pares = filter(is_par, numeros)
print(list(numeros_pares))


# otra forma mas optima con lambda 
numeros_impares = filter(lambda num: num % 2 == 1, numeros)
print(list(numeros_impares))
