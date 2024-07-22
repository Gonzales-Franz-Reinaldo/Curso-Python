# NOTA: 
#     - cuando solo hereda una clase de otra se llama herencia simple
#     - cuando dos clases heredan de una clase se llama herencia jerarquica
#     - cuando una clase hereda de dos clases se llama herencia multiple


class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"Hola, el que se encuentra hablando es: {self.nombre}")
        


# Herencia jerarquica cuando dos clases heredan de persona 
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, sueldo):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.sueldo = sueldo
        
    

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, grado, nota):
        super().__init__(nombre, edad, nacionalidad)
        self.grado = grado
        self.nota = nota


carlos = Empleado("Carlos", 23, "Boliviano", "Inge", 2334)

carlos.hablar()
print(carlos.nombre)