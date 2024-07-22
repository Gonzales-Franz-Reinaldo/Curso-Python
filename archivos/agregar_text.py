# para agregar un texto en el archivo de texto 
with open('archivos\\texto.txt', 'a', encoding='utf-8') as archivo:
   
    # para agregar texto en el archivo
    archivo.write('\n')
    
    for i in range(5):
        # agregando lineas 
        archivo.write(f'Hola {i} \n')