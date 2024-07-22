# para sobreescribir un texto en el archivo de texto 
with open('archivos\\texto.txt', 'w', encoding='utf-8') as archivo:
    # para sobreescribir en el arcivo 
    # archivo.write('Franz reinaldo gonzales suyo')
    
    # para escribir lineas agragando dos lineas 
    archivo.writelines(['- Hola mundo \n', '- Me la pelan'])