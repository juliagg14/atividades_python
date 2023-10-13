class Voo:
    def __init__(self, numero_voo, origem, destino, capacidade):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.capacidade = capacidade
        self.assentos_disponiveis = capacidade
        self.reservas = []

    def verificar_disponibilidade(self):
        return self.assentos_disponiveis

    def fazer_reserva(self, passageiro):
        if self.assentos_disponiveis > 0:
            self.reservas.append(passageiro)
            self.assentos_disponiveis -= 1
            print(f"Reserva para {passageiro.nome} no voo {self.numero_voo} foi feita com sucesso.")
        else:
            print("Desculpe, não há assentos disponíveis para esta reserva.")

    def cancelar_reserva(self, passageiro):
        if passageiro in self.reservas:
            self.reservas.remove(passageiro)
            self.assentos_disponiveis += 1
            print(f"Reserva de {passageiro.nome} no voo {self.numero_voo} foi cancelada.")
        else:
            print(f"{passageiro.nome} não tem reserva neste voo.")

class Passageiro:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def emitir_bilhete(self, voo):
        if self in voo.reservas:
            print(f"Bilhete de embarque para {self.nome} no voo {voo.numero_voo}: {voo.origem} para {voo.destino}.")
        else:
            print(f"{self.nome} não possui uma reserva neste voo.")

# Exemplo de uso do sistema de reservas de voos com interatividade
while True:
    print("\nOpções:")
    print("1 - Verificar disponibilidade de voos")
    print("2 - Fazer uma reserva")
    print("3 - Cancelar uma reserva")
    print("4 - Emitir bilhete de embarque")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        numero_voo = input("Digite o número do voo: ")
        origem = input("Origem: ")
        destino = input("Destino: ")
        capacidade = int(input("Capacidade total de passageiros: "))
        voo = Voo(numero_voo, origem, destino, capacidade)
        disponibilidade = voo.verificar_disponibilidade()
        print(f"Há {disponibilidade} assentos disponíveis no voo {voo.numero_voo} de {voo.origem} para {voo.destino}.")

    elif escolha == "2":
        nome = input("Nome do passageiro: ")
        sobrenome = input("Sobrenome do passageiro: ")
        cpf = input("CPF do passageiro: ")
        passageiro = Passageiro(nome, sobrenome, cpf)
        numero_voo = input("Digite o número do voo para a reserva: ")
        voo = Voo(numero_voo, "", "", 0)  # Voo temporário apenas para verificar disponibilidade
        disponibilidade = voo.verificar_disponibilidade()
        if disponibilidade > 0:
            voo.fazer_reserva(passageiro)

    elif escolha == "3":
        cpf = input("Digite o CPF do passageiro para cancelar a reserva: ")
        numero_voo = input("Digite o número do voo da reserva: ")
        passageiro = Passageiro("", "", cpf)
        voo = Voo(numero_voo, "", "", 0)  # Voo temporário apenas para cancelar reserva
        voo.cancelar_reserva(passageiro)

    elif escolha == "4":
        cpf = input("Digite o CPF do passageiro para emitir o bilhete de embarque: ")
        numero_voo = input("Digite o número do voo da reserva: ")
        passageiro = Passageiro("", "", cpf)
        voo = Voo(numero_voo, "", "", 0)  # Voo temporário apenas para emitir bilhete de embarque
        passageiro.emitir_bilhete(voo)

    elif escolha == "5":
        print("Voce finalizou o programa!!!")
        break
