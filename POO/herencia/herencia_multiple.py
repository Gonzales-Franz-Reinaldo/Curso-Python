
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"Hola, el que se encuentra hablando es: {self.nombre}")
        


class Deportista:
    def __init__(self, profesion, habilidad):
        self.profesion = profesion
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return (f"La habilidad que tiene el deportista es ser: {self.habilidad}")


class Futbolista(Persona, Deportista):
    def __init__(self, nombre, edad, nacionalidad, profesion, habilidad, dorsal, posicion):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Deportista.__init__(self, profesion, habilidad)
        self.dorsal = dorsal
        self.posicion = posicion
        
    def jugar(self):
        print(f"El Deportista {self.nombre} es un {self.profesion} y {super().mostrar_habilidad()}")



carlos = Futbolista("Carlos", 23, "Boliviano", "Futbolista", "Goleador", 7, "Delantero")

carlos.jugar()
carlos.hablar()

# para verificar si la clase es una subClase de otra clase 
herencia = issubclass(Futbolista, Deportista)

# para verificar si una objeto es una instancia de una clase
instancia = isinstance(carlos, Deportista)

print(instancia)