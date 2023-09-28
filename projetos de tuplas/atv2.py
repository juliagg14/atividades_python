num_alunos = int(input("Quantos alunos deseja registrar? "))
num_disciplinas = int(input("Quantas disciplinas deseja registrar? "))
alunos = []


for i in range(num_alunos):
    nome_aluno = input(f"Digite o nome do aluno {i+1}: ")
    notas_aluno = []
    for j in range(num_disciplinas):
        
        nota = float(input(f"Digite a nota do aluno {nome_aluno} na disciplina {j+1}: "))
        
        notas_aluno.append(nota)
        
    aluno = (nome_aluno, tuple(notas_aluno))
    
    alunos.append(aluno)

 
medias = []
for aluno in alunos:
    notas = aluno[1]
    media = sum(notas) / len(notas)
    medias.append((aluno[0], media))

 
medias.sort(key=lambda x: x[1])
maior_media = medias[-1]
menor_media = medias[0]


print("Alunos com a maior média:")

for aluno in medias:
    if aluno[1] == maior_media[1]:
        print(f"Nome: {aluno[0]}, Média: {aluno[1]}")

print("\nAlunos com a menor média:")

for aluno in medias:
    if aluno[1] == menor_media[1]:
        print(f"Nome: {aluno[0]}, Média: {aluno[1]}")