
#? OCP -> Principio de Abierto Cerrado 

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
    

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando un mensaje  por Email a {self.usuario.email}")
        

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando un mensaje por SMS a {self.usuario.sms}")

class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f"Enviando un mensaje por WhatsApp a {self.usuario.sms}")
        
        
# OCP -> Se refiere que las clases con metodos deben ser escalables y que no se pueda modificar la clase padre