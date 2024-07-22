# Existe varios tipos de polimosfismo como polimorfismo de inserción o de herencia

class Gato:
    def sonido(self):
        return "Miau"
        

class Perro:
    def sonido(self):
        return "Guao"

def hacer_sonido(animal):
    print(animal.sonido())


gato = Gato()
perro = Perro()

hacer_sonido(perro)

print(gato.sonido())


# en otros lenguajes como java, c++ este proceso funciona de diferente manera,
# se debe heredar el metodo para que existe polimorfisco como se ve el ejemplo 