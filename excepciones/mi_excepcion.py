# creando mi propooia excepcion 
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error {err}")
        
        
# manejandola
try:
    raise MiExcepcion("jajsa persona poca culta")
except:
    print("Como vas a cometer este error. ")