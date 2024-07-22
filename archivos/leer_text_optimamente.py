
# abriendo el archivo con with open 
with open('archivos\\texto.txt', encoding='utf-8') as archivo:
    # leemos el archivo 
    contenido = archivo.read()
    
print(contenido)

# no es necesario cerrar el archivo con close cuando aplicamos with 