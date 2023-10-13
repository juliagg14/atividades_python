class Funcionario:
    def __init__(self, nome, ID, salario):
        self.nome = nome
        self.ID = ID
        self.salario = salario

    def calcular_salario(self):
        return self.salario

    def promover(self, novo_salario):
        self.salario = novo_salario

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.ID}, Salário: R${self.salario:.2f}"


class Gerente(Funcionario):
    def __init__(self, nome, ID, salario, departamento):
        super().__init__(nome, ID, salario)
        self.departamento = departamento

    def promover(self, novo_salario, novo_departamento):
        super().promover(novo_salario)
        self.departamento = novo_departamento

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.ID}, Salário: R${self.salario:.2f}, Departamento: {self.departamento}"


class SistemaGestaoFuncionarios:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)

    def encontrar_funcionario_por_id(self, ID):
        for funcionario in self.funcionarios:
            if funcionario.ID == ID:
                return funcionario
        return None

    def dar_aumento(self, ID, aumento):
        funcionario = self.encontrar_funcionario_por_id(ID)
        if funcionario:
            novo_salario = funcionario.salario + aumento
            funcionario.promover(novo_salario)
            print(f"Aumento de R${aumento:.2f} dado a {funcionario.nome}")
        else:
            print(f"Funcionário com ID {ID} não encontrado.")

    def demitir_funcionario(self, ID):
        funcionario = self.encontrar_funcionario_por_id(ID)
        if funcionario:
            self.funcionarios.remove(funcionario)
            print(f"{funcionario.nome} foi demitido.")
        else:
            print(f"Funcionário com ID {ID} não encontrado.")


# Função para criar um novo funcionário com interatividade
def criar_funcionario():
    nome = input("Nome do funcionário: ")
    ID = input("ID do funcionário: ")
    salario = float(input("Salário do funcionário: "))
    tipo = input("Tipo de funcionário (Funcionário/Gerente): ").capitalize()

    if tipo == "Funcionario":
        funcionario = Funcionario(nome, ID, salario)
    elif tipo == "Gerente":
        departamento = input("Departamento do gerente: ")
        funcionario = Gerente(nome, ID, salario, departamento)
    else:
        print("Tipo de funcionário inválido.")
        return

    sistema.adicionar_funcionario(funcionario)
    print(f"{tipo} {nome} adicionado com sucesso!")


# Exemplo de uso do sistema de gestão de funcionários com interatividade
sistema = SistemaGestaoFuncionarios()

while True:
    print("\nOpções:")
    print("1 - Adicionar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Dar Aumento")
    print("4 - Demitir Funcionário")
    print("5 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        criar_funcionario()
    elif escolha == "2":
        sistema.listar_funcionarios()
    elif escolha == "3":
        ID = input("ID do funcionário para dar aumento: ")
        aumento = float(input("Valor do aumento: "))
        sistema.dar_aumento(ID, aumento)
    elif escolha == "4":
        ID = input("ID do funcionário para demitir: ")
        sistema.demitir_funcionario(ID)
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")