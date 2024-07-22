# import module_sald as salude

# importamos las funciones y le cambiamos los nombres
from module_sald import saludo, frases as frase

# importamos un modulos desde otro archivo separado una funcion 
import module.saludos as saludoss

saludo  = saludo('Calitos')
frase = frase('Hola mundo')

saludar = saludoss.sadular('Mario')

print(saludo)
print(frase)
print(saludar)

print(__name__)