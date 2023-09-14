contador = 0
maior = 0

while contador  < 5:
    numero = int(input ("digite um numero"))
    contador += 1
    print(numero)

    if numero > maior:
        maior = numero 


print("o maior numero é: ", maior)