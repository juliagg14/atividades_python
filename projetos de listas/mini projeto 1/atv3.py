import random

palavras =['cachorro', 'elefante', 'abelha ', 'leao', 'hipopotamo']
palavra = random.choice(palavras)
letras_certas = []
letras_erradas = []

while len(letras_erradas) < 6:
    letra = input("Digite uma letra")
    if letra in palavra:
        letras_certas.append(letra)
    else:
        letras_erradas.append(letra)
       
    palavra_atual = ''
    for letra_palavra in palavra:
        if letra_palavra in letras_certas:
            palavra_atual += letra_palavra
        else:
            palavra_atual += "_"

    print(palavra_atual)
    print("letras erradas:", letras_erradas)

    if letras_erradas == 6:
        print("Você perdeu! a palavra era", palavra)                

    if palavra_atual == palavra:
        print("Boua, acertou")
        break

   
   