voos_disponiveis = [
    ("V123", "São Paulo", "Rio de Janeiro", "2022-01-01", 250.00),
    ("V456", "São Paulo", "Brasília", "2022-02-01", 300.00),
    ("V789", "Rio de Janeiro", "Salvador", "2022-03-01", 400.00),
    ("V101", "São Paulo", "Recife", "2022-04-01", 350.00)
]

reservas = []
 
def listar_voos_disponiveis():
    print("Voos Disponíveis:")
    for voo in voos_disponiveis:
        print("Número do Voo:", voo[0])
        print("Origem:", voo[1])
        print("Destino:", voo[2])
        print("Data:", voo[3])
        print("Preço:", voo[4])
        print("-------------------------")

 

def reservar_passagem():
    numero_voo = input("Digite o número do voo desejado: ")
    for voo in voos_disponiveis:
        if voo[0] == numero_voo:
            reservas.append(voo)
            voos_disponiveis.remove(voo)
            print("Passagem reservada com sucesso!")
            return
    print("Número do voo inválido.")


def cancelar_reserva():
    numero_voo = input("Digite o número do voo da reserva a ser cancelada: ")
    for reserva in reservas:
        if reserva[0] == numero_voo:
            reservas.remove(reserva)
            voos_disponiveis.append(reserva)
            print("Reserva cancelada com sucesso!")
            return
    print("Número do voo inválido ou reserva não encontrada.")

 
def menu():
    print("1 - Listar voos disponíveis")
    print("2 - Reservar passagem")
    print("3 - Cancelar reserva")
    print("4 - Sair")
    

while True:
    
    menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        listar_voos_disponiveis()
    elif opcao == "2":
        reservar_passagem()
    elif opcao == "3":
        cancelar_reserva()
    elif opcao == "4":
        break

    else:
        print("Opção inválida. Tente novamente.")