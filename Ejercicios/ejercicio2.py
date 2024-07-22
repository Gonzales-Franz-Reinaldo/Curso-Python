texto  = input('Introduzca un texto: ')

palabras = texto.split(' ')
cantidad_palabras = len(palabras)

dalto_habla = 0.3

print(f'Mencionaste {cantidad_palabras} palabras y tardasre {cantidad_palabras / 2} seg. en decirlo')
print(f'Dalto lo diría en {cantidad_palabras / (2 * dalto_habla)} seg.')

if cantidad_palabras > 128:
    print('Para flaco tampoco abuses')