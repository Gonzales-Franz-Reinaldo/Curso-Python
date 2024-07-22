# creando una lista 
lista = list(['hola', 22, True, 'gonza', 45])
lista2 = list([2, 24, True, 8, 32, 12])

# longitud de una lista - devuelve la cantidad de elementos
longitud = len(lista)

# metodo para agregar un elemento a la lista en la ultima posi
lista.append('fran')

# agergar un elemento en la lista en una posición 
lista.insert(1, 'mundo')

# para agragar varios elementos a la lista 
lista.extend([10, 'Frgs'])

# para eliminar un elemento de la lista de un indice 
lista.pop(3)

# para eliminar un elemento de la lista por su valor 
lista.remove('fran')

# para eliminar todos los elementos de la lista y limpiarlo
# lista.clear()

# para ordenar una lista
lista2.sort()

# para invertir los elementos de una lista
lista2.reverse()

elemento_encontrado = lista.index('gonza')

print(dir(lista))
print(elemento_encontrado)