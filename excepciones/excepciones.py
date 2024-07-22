# crear una funcion que sume dos numeros introducidos
def sumar_dos():
    while True:
        a = input("Número 1: ")
        b = input("Número 2: ")
        
        # convertimos a enteros y sumamos
        try:
            resultado = int(a) + int(b)
            # si lanza una excepcion
        except ValueError as e:
            print("Te pedí un número no te hagas gracioso")
            print(f"ERROR: {e}")
        # si todo salio bien terminamos el bucle
        else:
            break
        finally:
            print("Manejo de excepcion terminado")
            
    return resultado

suma_total = sumar_dos()
print(f'La suma es: {suma_total}')