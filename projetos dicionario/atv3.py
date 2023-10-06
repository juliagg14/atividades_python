notas_alunos = {}

 

def registrar_notas():

    nome_aluno = input("Digite o nome do aluno: ")

    notas = []

    continuar = True

    while continuar:

        nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))

        if nota == -1:

            continuar = False

        else:

            notas.append(nota)

    notas_alunos[nome_aluno] = notas

 

def calcular_media(nome_aluno):

    notas = notas_alunos.get(nome_aluno)

    if notas:

        media = sum(notas) / len(notas)

        print(f"A média do aluno {nome_aluno} é {media}")

    else:

        print(f"Não foi encontrada nenhuma nota para o aluno {nome_aluno}")

 

opcao = ""

while opcao != "3":

   

    print("1- Registrar uma nova nota")

    print("2- Calcular a média de um aluno")

    print("3- Sair")

   

    opcao = input("O que você deseja fazer? ")

    if opcao == "1":

        registrar_notas()

    elif opcao == "2":

        nome_aluno = input("Digite o nome do aluno: ")

        calcular_media(nome_aluno)

    elif opcao == "3":

        print("Programa encerrado.")

    else:

        print("Opção inválida. Por favor, tente novamente.")