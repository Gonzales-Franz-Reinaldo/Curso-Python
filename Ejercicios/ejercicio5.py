# funcion para calcular el fibonacci

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
    
def serie_fibonacci(num):
    serie = []
    for i in range(num):
        serie.append(fibonacci(i))
    
    return serie


def calcular_fibonacci(num):
    a, b = 0, 1
    serie_fibonacci = [0]
    
    for i in range(num):
        if b > num:
            return serie_fibonacci
        else:
            serie_fibonacci.append(b)
            a, b = b, a + b
        
    return serie_fibonacci
        
resultado = calcular_fibonacci(34)
print(resultado)