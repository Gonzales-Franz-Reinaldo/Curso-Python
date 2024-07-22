# crear 2 listas una con nombres y otro con apellidos
nombres = ['Juan', 'Carlos', 'Franz', 'Cinthia', 'Samira']
apellidos = ['Peres', 'Torrez', 'Gonzales', 'Garcia', 'Diaz']

with open("problemas_archivos\\texto1.txt", "w") as archivo:
    archivo.writelines("Los datos son: \n\n")
    
    [archivo.writelines(f"Nombre: {n} \nApellido: {a}\n---------\n") for n, a in zip(nombres, apellidos)]