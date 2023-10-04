# Exercício 2: Contagem de Caracteres
'''Dado um texto, conte quantas vezes cada caractere aparece (incluindo 
espaços e caracteres especiais) e armazene os resultados em um 
dicionário.'''

def contar_caracteres(texto):

    contagens = {}

    for caracter in texto:
        if caracter in contagens:
            contagens[caracter] += 1

        else:
            contagens[caracter] = 0
    return contagens

texto = "to voltando para os rodeio"
contagem_caracter = contar_caracteres(texto)
print(contagem_caracter)  