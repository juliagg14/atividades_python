lista_numeros = []

for i in range(10):
    lista_numeros.append(int(input("digite um numero: ")))
    
print(lista_numeros)

def encontrar_menor_elemento(lista_numeros):
    menor = lista_numeros[0]
    for numero in lista_numeros:
        if numero < menor:
            menor = numero
            
    return menor

print('-------------------------------------')
print('MENOR:')
print(encontrar_menor_elemento(lista_numeros))