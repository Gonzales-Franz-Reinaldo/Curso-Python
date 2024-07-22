cadena1 = 'Hola, mundo, de, python'
cadena2 = 'de programación'
cadena3 = '23332'

# print(dir(cadena2))

minusculas = cadena1.lower()

mayusculas = cadena1.upper()

busq_find = cadena2.find('e')

busq_index = cadena2.index('p')

is_numeric = cadena3.isnumeric()

is_alpha = cadena2.isalpha()

# el metodo count cuenta la cantidad de coincidencias de una cadena dentro de una cadena 
contar_coincidencia = cadena2.count('a')

# imprime la longitud de una cadena 
longitud_cadena = len(cadena2)

empieza_con = cadena1.startswith('Ho')

termina_con = cadena1.endswith('do')

nueva_cadena = cadena2.replace('de', 'curso')

cadena_separada = cadena1.split(',')

# print(f'La cadena tiene una longitud de {longitud_cadena}')
print(cadena_separada[2])