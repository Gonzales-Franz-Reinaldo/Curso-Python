# creando un diccionario 
diccionario = dict(nombre = 'franz', apellido = 'Gonza', anio = 2024)

# las listas no pueden ser claves y usamos frozenset para meter conjuntos 
diccionario = {frozenset(['hola', 'mundo']): 'python'}

# creando un diccionario con fromkeys 
diccionario = dict.fromkeys(['mundo', 'de', 'programación'], 'nose')

print(diccionario)