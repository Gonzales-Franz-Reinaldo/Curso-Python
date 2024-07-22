# para importar paquetes y sub-paquetes el arcivo debe tener __init__.py para poder importar 

import paquete.frases2

# print(paquete.__path__)
resultado = paquete.frases2.frases('Gonzales')

print(resultado)