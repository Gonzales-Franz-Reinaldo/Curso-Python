import re

# la cadena con la fecha y el telefono 
text = "La fecha es 23/06/2321 y el teléfono es +1-555-555-5555"

# el patron a buscar 
pattern = r"\d{2}/\d{2}/\d{4}"

# el patron a rempazar
replacement_pattern = "Fecha oculta"

# remplazamos todas las apariciones en la cadena con los patrones
new_text = re.sub(pattern, replacement_pattern, text)

print("Texto modificado es: ", new_text)