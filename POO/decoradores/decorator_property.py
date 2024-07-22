class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        
    # para eliminar un propiedad 
    @nombre.deleter
    def nombre(self):
        del self.__nombre

dalto = Persona("Juan", 23)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "Pepe"
nombre = dalto.nombre

print(nombre)

del dalto.nombre

print("Que haces jilipollas.")