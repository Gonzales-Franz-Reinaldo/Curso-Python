import pandas as pd 

df = pd.read_csv("problemas_archivos\\datos.csv")

# convertir a string todos los datos de una columna
df["Edad"] = df["Edad"].astype(str)

# mostrando el typo de dato de la columna cambiado de tipo de dato 
# print(type(df["Edad"][0]))

# remplazando los datos "Garcia" por Gonzales
df["Apellido"].replace("García", "Gonzales", inplace=True)

# print(df)

# mostrando la columna de apellidos 
# print(df["Apellido"])

# eliminando las filas con datos faltantes
df = df.dropna()

# eliminando las filas repetidas 
df = df.drop_duplicates()

# creando un CSV en dataframe con el resultante (limpio)
df.to_csv("problemas_archivos\\datos_limpio.csv")

# print(df)