# funtcion optima para sumar
def suma_total(numeros):
    return sum(*[numeros])

suma = suma_total([12, 23, 4, 5, 3, 10])
print(suma)

# otra forma de sumar aplicando el operador *  como parametro (*args)
def suma(nombre, *numeros):
    suma_total = sum(numeros)
    return f'La suma total es: {suma_total} y tu nombre es {nombre}'


resultado = suma('Franky', 2, 43, 52, 12, 10)
print(resultado)