animales = {'gato', 'perro', 'loro', 'tigre', 'gallina'}
numeros = {23, 42, 5, 7, 34}

for i in animales:
    print(i)

for num in numeros:
    multiplo = num * 10
    print(f'Multiplo es: {multiplo}')
    

# iterando dos conjunto al mismo tiempo
for animal, num in zip(animales, numeros):
    print(f'Animal # {animal}')
    print(f'Número = {num}')
    

for i in range(5, 20, 2):
    print(i)

# forma no adecuada para recorrer una conjunto 
# for num in range(len(numeros)):
#     print(f'num = {numeros[num]}')


# forma correcta de recorrer una conjunto 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El índice es {indice} y el valor es {valor}')
    

# otra forma de recorrer una conjunto con for/esle (el else solo se ejecuta sola una vez)
for j in animales:
    print(f'animal = {j}')
else:
    print('Se ha terminado de recorrer la conjunto')

#todo: Tanto para conjuntos y tuplas funciona lo mismo en la iteración