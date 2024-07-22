
#? Principio de Segregación de la Interfaz 

from abc import ABC, abstractmethod

# dividimos en subInterfaces para que  exista dependencias propias 
class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass # pass se aplica para si o si debe ser heredado o a[licado el metodo de la clase padre
    
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass



class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print("El humano esta comiendo")
    
    def trabajar(self):
        print("El humano esta trabajando")
    
    def dormir(self):
        print("El humano esta durmiendo")
        

class Robot(Trabajador):
    
    def trabajar(self):
        print("El robot esta trabajando")


robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
humano.dormir()
humano.comer()