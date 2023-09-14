dias = int(input("quer medir a tempeatura de quantos dias: "))
contador= 0 
soma= 0
maior= 0 
menor= 0


while contador < dias:
    temperatura = int(input("informe a temperatura: "))
    contador += 1
    print(temperatura)


    soma = soma + temperatura


if temperatura > maior:
    maior = temperatura
elif menor < maior:
    menor = temperatura

media = float(soma / dias)

print("a temperatura maior foi de: ", maior )
print ("a menor temperatura foi de: ", menor)
print( "a media das temperaturas dos dias foi de: {:.1f}° ".format (media))