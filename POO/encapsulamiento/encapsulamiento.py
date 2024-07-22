
# los atributos privados son cuando tienen __ en el atributo y los mismo para los metodos 
class MiClase:
    def __init__(self):
        self.__atributo_privado = "Caray"
        
    def __hablar(self):
        print("Hola")

objecto = MiClase()

objecto._hablar()
# print(objecto.__atributo_privado)