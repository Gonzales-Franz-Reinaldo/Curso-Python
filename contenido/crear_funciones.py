# funciones 

def saludo(nombre, sexo):
    sexo = sexo.lower()
    if sexo == 'mujer':
        adjetivo = 'reina'
        print(f'Hola {nombre} mi {adjetivo} como va.')
    elif sexo == 'hombre':
        adjetivo = 'carnal'
        print(f'Que honda {nombre} que va mi {adjetivo}')
    else:
        adjetivo = 'amor'
        print(f'que tal {nombre} mi {adjetivo}.')
        
saludo('franz', 'hombre')
saludo('cinthia', 'MUJER')


# funcion para crear una contraseña randon
def contraseña_random(num):
    chars = 'hasokdosrt'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    password = f'{num * 2}{chars[c1]}{chars[c2]}{chars[c3]}'
    return password, num

contraseña, numero = contraseña_random(734)
print(f'Tun contraseña es: {contraseña} \nY el número aplicado es: {numero}')


# otro tipo de funciones 
def frase(nombre, apellido, adjetivo = 'hombre'):
    return f'Hola {nombre} {apellido} que onda {adjetivo}'

resultado = frase('Frank', 'Perez', 'carnal')
print(resultado)