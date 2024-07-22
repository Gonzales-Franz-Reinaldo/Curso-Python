#clases 

class Celular:
    def __init__(self, marca, modelo, camara):
        # atributos
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    
    # metodos 
    def llamar(self):
        print(f"Realizaste una llamada desde el movil {self.modelo}")
        
    def cortar_llamada(self):
        print(f"Cortaste la llamada desde tu movil {self.modelo}")



celular1 = Celular("Xiaomi", "Redmi Note 9 Pro", "64MP")
celular2 = Celular("Samsung", "A51", "48MP")


celular1.llamar()
celular2.cortar_llamada()




#? EJEMPLO BÁSICO  
class CelularE():
    marca = "Samsung"
    modelo = "S23"
    camara = "64MP"

celular1 = CelularE()
celular2 = CelularE()

# print(celular1.marca)
# print(celular2.modelo)
