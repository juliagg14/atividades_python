pergunta = input("digite uma palavra: ").lower()
pergunta = tuple(str(pergunta))
print (pergunta)

contador = 0 
contador_vogais = 0
contador_consoantes = 0
quantidade_letras = len(pergunta)
vogais = ['a', 'e', 'i', 'o', 'u']



for contador in range (quantidade_letras):
    if pergunta[contador] == ' ':
        pass
    elif pergunta[contador] in vogais:
        contador_vogais += 1
    else:
        contador_consoantes += 1
        
print(f'a palavra tem : [{contador_vogais} vogais] é : [{contador_consoantes} consoantes]' )