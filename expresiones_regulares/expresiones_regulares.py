import re

texto = '''Hola mundo como. estan todos aqui, esta es la cadena 1 mundo
Esta es la segunda cadena 345 , esta es la tercera cadena 3. y
Esta es la segunda cadena _2, esta es la tercera cadena 31. y mundo
Como siempre practicando. la programación jasa'''

# busca la cadena dentro del texto 
resultado = re.search("Hola", texto)

# para buscar todos los palabras sin importar mayusculas y minusculas dentro de la cadena 
busqueda_cadena = re.findall("Esta", texto, flags=re.IGNORECASE)

# EXPRESIONES REGULARES 

# \d -> busca todos los digitos numéricos dentro de una cadena del 0 - 9
digitos = re.findall(r"\d", texto)

# \D -> para buscar todo una busqueda general meno los digitos del 0 - 9
busqueda_general = re.findall(r"\D", texto)

# \w -> busqueda de caracteres alfanuméricos [a-z A-Z, 0-9, _]
busqueda_caracter_alfanumericos = re.findall(r"\w", texto)

# \W -> busca TODO menos los caracteres alfanuméricos [a-z A-Z, 0-9, _]
busqueda_caracter_no_alfanumericos = re.findall(r"\W", texto)

# \s -> busca los espacios en blanco, espacios tabs, saltos en linea
espacios_blanco = re.findall(r"\s", texto)

# \S -> busca TODO menos los espacios en blanco espacios tabs, saltos en linea
busq_todo_menos_espaBlanco = re.findall(r"\S", texto)

# . -> busca TODO meno los saltos de linea 
busq_todo = re.findall(r".", texto)

# \n -> busca los saltos de linea 
saltos_linea = re.findall(r"\n", texto)

# \ -> cancelar caracteres especiales, ejemp: cancelando la funcion del punto y buscando puntos 
puntos = re.findall(r"\.", texto)


# armando una cadena que busque un numero seguido de un punto y un espacio 
resultado = re.findall(f"\d\.\s", texto)

# ^ -> busca el comienzo de una ejemp: (buscando 'Hola' al principio de la linea) 
# flags=re.M activa las multilineas 
comienzo_linea = re.findall(f"^Esta", texto, flags=re.M)

# $ -> busca el final de la linea 
final_linea = re.findall(f"mundo$", texto, flags=re.M)

# {n} -> busca n cantidad de veces el valor de la izquierda (3 numeros juntos esta vez)
n_cantidad= re.findall(r"\d{3}", texto)

# {n, m} -> al menos n, maximo m 
rango_cantidad = re.findall(r'\d{2,4}', texto)

# | -> busca una cosa o la otra cosa
busq_or = re.findall(r'\d{2,3}|Hola', texto)

print(busq_or)