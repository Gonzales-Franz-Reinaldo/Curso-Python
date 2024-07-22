# Si el modulo estuviero dentro de la misma carpeta en la misma ruta
# import module.saludos as saludo

# cuando el modulo esta afuera de los demas modulos en otra carperta
import sys

sys.path.append('c:\\Curso Python\\prueba_module')

import frases as frase 

# resultado = saludo.sadular('Hola mundo')

# print(saludo.sadular('franco'))

print(frase.mostrar_frase('Hola mundo'))