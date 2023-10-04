# Exercício 1: Contagem de Palavras com Lista de Frases
'''Dado um dicionário de informações de alunos, escreva um programa que 
filtre os alunos que têm uma nota superior a 85 e crie um novo dicionário 
com esses alunos.'''


dados_alunos = {
    "joao" : 80,
    "julia": 90,
    "carol": 85,
    "victor": 79
}

aprovados = {}

for nome, nota in dados_alunos.items():
  if nota >=85:
    aprovados[nome] = nota

print(aprovados)