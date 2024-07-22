import pandas as pd 

# usando la funcion read_csv para leer un archivo csv 
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

# leyendo solo la columna de nombres 
nombres = df['Nombre']

# trabajando con eslaisin 
cadena = '0123456789'

print(cadena[0:7])

# para ordenar los datos por la edad 
df_orden_ascendente = df.sort_values("Nombre")

# para ordenar descendentemente por el nombre 
df_orden_descendentemente = df.sort_values("Nombre", ascending=False)


# para concatenar los dos dataframes
df_concatenado = pd.concat([df, df2])

# accediendo a la primera fila del dataframe con head()
primera_fila = df.head(2)  # muestra las dos primeras filas

# accediendo a las ultimas filas con tail()
ultima_filas = df.tail(2)

# accediendo a la cantidad de filas y columnas con shape
filas, columnas = df.shape

# para obtener la data estadistica del dataframe 
data_info = df.describe()

# accediendo al nombre de la fila 2 con loc 
elemento_espec_loc = df.loc[2, "Nombre"]

# accediendo al nombre de la fila 2 con iloc 
elemento_espec_iloc = df.iloc[2, 2]

# accediendo a todas las filas de una columna con iloc
nombres = df.iloc[:,0]

# accediendo a todas las filas de una columna con loc
nombres_loc = df.loc[:, "Nombre"]

# accediendo a la fila 3 con los loc 
fila_3 = df.loc[2,:]

# accediendo a la fila 3 con los iloc 
fila_3 = df.iloc[2,:]

# accediendo a las filas de nombres que sean diferentes de luis
dif_nombre = df.loc[df["Nombre"] != "Ana", :]

print(dif_nombre)
