
text_ = open("archivos\\texto.txt", encoding='UTF-8')

# para leer todo el archivo 
# archivo = text_.read()

# para leer una sola linea 
# archivo = text_.readline()

# para leer linea por linea
archivo = text_.readlines()

# para cerrar el archivo 
text_.close()

print(archivo)