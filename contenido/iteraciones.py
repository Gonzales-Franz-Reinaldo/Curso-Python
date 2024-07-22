
frutas = ['banana', 'pera', 'mango', 'durazno', 'manzana']
cadena = 'Hola mundo'
numeros = [2, 3, 5, 6, 7, 9]

# evitando que se aplique un elemento con la secuencia continue 
for fruta in frutas:
    if fruta == 'mango':
        continue
    print(f'me voy a comer una {fruta}')
    
# break hace que termine el ciclo 
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'durazno':
        break
else:
    print('bucle terminado')

# recorriendo una cadena 
for letra in cadena:
    print(letra)
    

# ciclo for en una sola linea
numero = [x ** 2 for x in numeros]

print(numero)