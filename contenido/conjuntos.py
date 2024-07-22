# creand un conjunto set 
conjunto = set(["Dato 1"])

# metiendo un conjunto a otro conjunto
conjunto1 = frozenset(['hola', 'mundo'])
conjunto2 = {conjunto1, 'dato 1'}

# print(conjunto2)

# teoria de conjuntos 
conjunto1 = {1, 3, 5 ,7}
conjunto2 = {2, 4, 6, 8}

# verificamos si es un subconjunto 
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

# verificamos si es un superconjunto
resultado2 = conjunto1.issuperset(conjunto2)
resultado2 = conjunto2 > conjunto1

# verificar si hay un numero en comun 
resultado3 = conjunto2.isdisjoint(conjunto1)

print(resultado3)