class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre


gonza = Persona("Juan", 23)

nombre = gonza.get_nombre()
print(nombre)

gonza.set_nombre("Carlos")
nombre = gonza.get_nombre()

print(nombre)