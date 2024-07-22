
# Keys() -> devuelve las claves - tambien nos sirve para iterar
# get() -> devuelve el valor de una clave
# clear() -> elimina todos los elementos
# pop() -> elimina un elemento
# items() -> para iterar el dict

diccionario = {
    'nombre': 'franz',
    'apellido': 'gonzales',
    'edad': 21,
    'sex': 'M'
}

claves = diccionario.keys()

valor = diccionario.get('nombre')

# diccionario.clear()

diccionario.pop('sex')

dic_item = diccionario.items()

print(dic_item)