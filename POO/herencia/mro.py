# Método de Resolución de Orden

class A:
    def hablar(self):
        print("Hola des A")

class F:
    def hablar(self):
        print("Hola des F")

class B(A):
    def hablar(self):
        print("Hola des B")

class C(F):
    def hablar(self):
        print("Hola des C")

class D(B, C):
    def hablar(self):
        print("Hola des D")
        

d = D()

# para mostra el metodo hablar desde diferentes clases 
B.hablar(d)

# print(D.mro())