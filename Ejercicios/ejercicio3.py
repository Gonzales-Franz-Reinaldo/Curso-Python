# El profe falto a clases y los compañeros arman la clase 

def armar_clase(cantidad_alumnos):
    compañeros = []
    for i in range(cantidad_alumnos):
        nombre = input('Nombre del alumno: ')
        edad = int(input('Edad del alumno: '))
    
        alumno = (nombre, edad)
        compañeros.append(alumno)

    compañeros.sort(key=lambda x : x[1])
    
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    return asistente, profesor


asistente, profesor = armar_clase(5)

print(f'El profesor es {profesor} y su asistente es {asistente}')

