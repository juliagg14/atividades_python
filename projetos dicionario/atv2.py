agenda_de_contatos = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o endereço de email: ")
    agenda_de_contatos[nome] = {"Telefone": telefone, "Email": email}
    print(f"Contato {nome} adicionado com sucesso!")

def visualizar_contato():
    nome = input("Digite o nome do contato que deseja visualizar: ")
    contato = agenda_de_contatos.get(nome)
    if contato:
        print(f"Nome: {nome}")
        print(f"Telefone: {contato['Telefone']}")
        print(f"Email: {contato['Email']}")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

def editar_contato():
    nome = input("Digite o nome do contato que deseja editar: ")
    contato = agenda_de_contatos.get(nome)
    if contato:
        novo_telefone = input("Digite o novo número de telefone: ")
        novo_email = input("Digite o novo endereço de email: ")
        contato['Telefone'] = novo_telefone
        contato['Email'] = novo_email
        print(f"Contato {nome} editado com sucesso!")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ")
    if nome in agenda_de_contatos:
        del agenda_de_contatos[nome]
        print(f"Contato {nome} excluído com sucesso!")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Visualizar Contato")
        print("3. Editar Contato")
        print("4. Excluir Contato")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            visualizar_contato()
        elif escolha == '3':
            editar_contato()
        elif escolha == '4':
            excluir_contato()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()