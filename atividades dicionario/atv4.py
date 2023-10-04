#Exercício 4: Dicionário de Dicionários
'''Modifique o exercício anterior para criar um dicionário de dicionários, 
onde cada aluno é representado por um dicionário contendo idade e 
nota.'''


dados_alunos = {
    "nomes": ["julia", "joao", "victor", "jessika", "carol"],
    "idades": [19, 18, 27, 29, 29],
    "notas": [80, 60, 70, 65, 85]
}

alunos = {}

for nome, idade, nota in zip(dados_alunos["nomes"], dados_alunos["idades"], dados_alunos["notas"]):
    alunos[nome] = {'idade': idade, 'nota': nota}

print(alunos)