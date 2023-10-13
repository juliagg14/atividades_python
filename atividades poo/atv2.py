class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


estudantes = []


while True:
    print("\nEscolha uma opção:")
    print("1 - Criar Estudante")
    print("2 - Adicionar Nota")
    print("3 - Calcular Média")
    print("4 - Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        nome = input("Digite o nome do estudante: ")
        matricula = input("Digite a matrícula do estudante: ")
        estudante = Estudante(nome, matricula)
        estudantes.append(estudante)
    elif escolha == "2":
        if not estudantes:
            print("Nenhum estudante criado. Crie um estudante primeiro.")
        else:
            print("Estudantes disponíveis:")
            for i, estudante in enumerate(estudantes):
                print(f"{i + 1} - {estudante.nome} ({estudante.matricula})")

            escolha_estudante = int(input("Selecione o estudante: ")) - 1
            nota = float(input("Digite a nota a ser adicionada: "))
            estudantes[escolha_estudante].adicionar_nota(nota)
    elif escolha == "3":
        if not estudantes:
            print("Nenhum estudante criado. Crie um estudante primeiro.")
        else:
            print("Estudantes disponíveis:")
            for i, estudante in enumerate(estudantes):
                print(f"{i + 1} - {estudante.nome} ({estudante.matricula})")

            escolha_estudante = int(input("Selecione o estudante: ")) - 1
            media = estudantes[escolha_estudante].calcular_media()
            print(f"A média do estudante {estudantes[escolha_estudante].nome} é {media:.2f}")
    elif escolha == "4":
        print("Saindo do programa. Obrigado!")
        break
 