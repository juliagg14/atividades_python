import random

faces_do_dado = (1, 2, 3, 4, 5, 6)

input("precione enter lara lançar o dado...")
numero_aleatorio = random.choice(faces_do_dado)

numero_escolhido = int(input(" escolha um numero entre 1 e 6: "))

if numero_escolhido in faces_do_dado:
    if numero_escolhido == numero_aleatorio:
        print(f"voce ganhou! o numero{numero_aleatorio} corresponde ao numero gerado.")
        
    else:
        
        print(f"voce perdeu! o numero gerado foi {numero_aleatorio}.")
        
else:
    print("por favor, escolha um numero valido de 1 a 6!") 