class Estudiante:
    def __init__(self, nombre, apellido, edad, grado):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.grado = grado
        
    # metodos del estudiante 
    def estudiar(self):
        print(f"El estudiante {self.nombre} se encuentra estudiando.")
        
    def hacer_tarea(self, tarea):
        if tarea == "SIS256":
            print(f"El estudiante {self.nombre} hace la tarea de {tarea}")
        else:
            print(f"La tarea no es de la materia que llevas")
            

nombre = input('Nombre del estudiante: ')
apellido = input('Apellido del estudiante: ')
edad = input('La edad del estudiante: ')
grado = input('El grado es: ')

estudiante1 = Estudiante(nombre, apellido, edad, grado)

print(f"""
    Datos del Estudiante:\n\n
    Nombre: {estudiante1.nombre}\n
    Apellido: {estudiante1.apellido}\n
    Edad: {estudiante1.edad}\n
    Grado: {estudiante1.grado}\n
    """)

estado = input()

if estado.lower() == 'estudiar':
    estudiante1.estudiar()
elif estado.lower() == 'hacer tarea':
    estudiante1.hacer_tarea('SIS256')
else:
    print('No coincide vuelve a escribir')
    estado = input()
    