def calcular_media(lista):
    if len(lista) == 0:
        return 0 
    
    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = []
quantidade = int(input("quantos numeros quer adicionar?"))

for i in range (quantidade):
    numero = float(input("digite o numero: "))
    numeros.append(numero)
    
media = calcular_media(numeros)
print(media)