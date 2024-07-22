
#? SRP -> Principio de Responsabilidad Unica 

class  TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
        
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
        

class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Haz movido existosamente el auto")
        else:
            print("No hay suficiente combustible.")
    
    def obtener_posicion(self):
        return self.posicion
    

tanque = TanqueDeCombustible()
auto = Auto(tanque)

auto.mover(40)
print(auto.obtener_posicion())
auto.mover(70)
print(auto.obtener_posicion())
auto.mover(90)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())
