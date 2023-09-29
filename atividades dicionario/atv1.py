print("------------alunos-----------")

alunos = {
"julia": 85,
"lucas": 90,
"victor":80,
"joao": 82
}
print(alunos)
    
print("------------aprovados-----------")

aprovados = {}

for nomes, notas in alunos.items():
 if notas >= 85:
  aprovados[nomes]= notas
 
print(aprovados)