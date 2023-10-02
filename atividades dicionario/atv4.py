#Exercício 4: Dicionário de Dicionários
'''Modifique o exercício anterior para criar um dicionário de dicionários,
onde cada aluno é representado por um dicionário contendo idade e
nota.'''



dados_alunos = {
"julia": {'idade':19, 'nota': 80},
"joao": {'idade':15, 'nota': 90},
"victor":{'idade':27, 'nota':85},
"carol": {'idade':20, 'nota':70}
                
}


print(dados_alunos.keys)



for nomes, idades, notas in zip(dados_alunos["nomes"], dados_alunos["idades"], dados_alunos["notas"]):
 print(f"nome: {nomes} - idade:{idades} - nota: {notas}")