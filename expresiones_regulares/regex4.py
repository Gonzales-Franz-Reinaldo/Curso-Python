# para validar un correo electrónico

import re

email = "gonzalesfranz2019@gmail.com"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

if result:
    print('Dirección de correo válido')
else:
    print('Dirección de correo no válida')