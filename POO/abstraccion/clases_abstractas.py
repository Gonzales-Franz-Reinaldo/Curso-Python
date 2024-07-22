
# las clases abstractas no se pueden onstanciar a un objeto y sirver para crear otras clases son como plantillas
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod  # con esto estamos obligando a las clases que lo implementen los metodos
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
        


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Mi actividad es: {self.actividad}")
        

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de {self.actividad}")


persona = Estudiante("Juan", 22, "Masculino", "Programación")
dalto = Trabajador("Carlos", 23, "Masculino", "Programación")

persona.presentarse()
persona.hacer_actividad()

dalto.presentarse()
dalto.hacer_actividad()