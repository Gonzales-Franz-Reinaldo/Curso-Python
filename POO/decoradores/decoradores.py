# los decoradores son cuando envias otra funcion para agregar a otra funcion antes o despues de ejecutarlo
def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
    return funcion_modificada

# def saludo():
#     print("Hola mundo")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()


# otro mas optimo 
@decorador
def saludo():
    print("Hola mundo")

saludo()