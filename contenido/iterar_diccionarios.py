diccionario = {
    'nombre': 'franz',
    'apellido': 'gonzales',
    'edad': 21,
    'sex': 'M'
}

for item in diccionario:
    print(item)
    
    
for item in diccionario.items():
    key = item[0]
    valor = item[1]
    print(f'El key es {key} y el valor es {valor}')