# para leer archivos csv de datos 
import csv

with open("archivos\\datos.csv", encoding='utf-8') as archivo:
    reader = csv.reader(archivo)
    
    for i in reader:
        print(i)