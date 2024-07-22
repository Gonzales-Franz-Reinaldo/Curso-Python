# numeros primos de 0 al numero introducido
def es_primo(num):
    if num < 2:
        return False
    
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True

def numeros_primos(num):
    numeros_primos = []
    
    for i in range(2, num + 1):
        primo = es_primo(i)
        if primo == True:
            numeros_primos.append(i)
            
    
    return numeros_primos

primos = numeros_primos(51)
print(primos)


# otra forma mas optimizada 
num_primos = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))

# num_primos = lambda num: list(
#     filter(
#         lambda x: all(
#             x % i != 0 for i in range(2, int(x ** 0.5) + 1)
#             ), range(2, num)
#         )
#     )

print(f'Número primos son {num_primos(51)}')