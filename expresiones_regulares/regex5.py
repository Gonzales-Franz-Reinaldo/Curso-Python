# validando direcciones de paginas

import re 

direccion = "Este es el ejemplo de una página web https://proyectodalto.com o tambien pode ver otras."

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, direccion)

print(result)