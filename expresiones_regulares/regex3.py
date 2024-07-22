import re 

text = 'Remplazando todas las vocales por los ascteriscos'

resultado = re.sub("[aeiou]", "*", text)

print(resultado)