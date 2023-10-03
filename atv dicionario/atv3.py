# Exercício 3: Combinação de Dicionários com Listas
'''Crie um programa que combine dicionários com informações de alunos,
incluindo nome, idade e notas. Os dados estão armazenados em listas
separadas.'''

dados_alunos = {

    "nomes": ["julia","joao", "victor","jessika", "carol"],

    "idades": [19,18, 27, 29, 29],

    "notas": [80, 60, 70, 65, 85]

}

for nomes, idades, notas in zip(dados_alunos["nomes"], dados_alunos["idades"], dados_alunos["notas"]):
    print(f"nome: {nomes} - idade:{idades} - nota: {notas}")