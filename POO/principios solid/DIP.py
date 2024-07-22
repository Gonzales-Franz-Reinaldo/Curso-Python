
#? Principio de Inversión de Dependencia 

# Contexto: En este caso un ejemplo en las clases es que una clase grande e importante 
# no deberia depender de una simple o pequeña clase 

# class Diccionario:
#     def verificar_palabra(self, palabra):
#         # logica para verificar palabra 
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         # usamos el Diccionario para corregir el texto 
#         pass


from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # logica para verificar palabras si estan en el Diccionario
        pass
    
class ServicioWeb(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # logica para verificar palabras si estan en el Pagina web
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        # usamos el verificador para corregir el texto
        pass
    

corrector = CorrectorOrtografico(Diccionario())