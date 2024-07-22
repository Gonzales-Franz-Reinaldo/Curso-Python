import re

numero = "Hola Gonzales, mi número es: +951 7286-3820 +951 7286-3820"

pattern = r"\+\d{3}\s\d{2,}-\d{3,}"

num_remplazo = re.sub(pattern, "(Número oculto)", numero)

print(num_remplazo)