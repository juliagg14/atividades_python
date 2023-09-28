livros = []


def listar_livros():
    print("Livros Disponíveis:")
    for livro in livros:
        print("Título:", livro[0])
        print("Autor:", livro[1])
        print("Preço:", livro[2])
        print("Quantidade em Estoque:", livro[3])
        print("-------------------------")
        

def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    preco = float(input("Digite o preço do livro: "))
    quantidade = int(input("Digite a quantidade em estoque do livro: "))
    livro = (titulo, autor, preco, quantidade)
    livros.append(livro)
    print("Livro adicionado com sucesso!")

 

def remover_livro():
    titulo = input("Digite o título do livro a ser removido: ")
    for livro in livros:
        if livro[0] == titulo:
            livros.remove(livro)
            print("Livro removido com sucesso!")
            
            return
    print("Livro não encontrado.")
 

def atualizar_livro():
    titulo = input("Digite o título do livro a ser atualizado: ")
    for livro in livros:
        if livro[0] == titulo:
            novo_titulo = input("Digite o novo título do livro: ")
            novo_autor = input("Digite o novo autor do livro: ")
            novo_preco = float(input("Digite o novo preço do livro: "))
            nova_quantidade = int(input("Digite a nova quantidade em estoque do livro: "))
            livro = (novo_titulo, novo_autor, novo_preco, nova_quantidade)
            print("Livro atualizado com sucesso!")
            
            return
    print("Livro não encontrado.")


def menu():
    print("1 - Listar livros disponíveis")
    print("2 - Adicionar livro")
    print("3 - Remover livro")
    print("4 - Atualizar livro")
    print("5 - Sair")

 
while True:

    menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        listar_livros()

    elif opcao == "2":
        adicionar_livro()

    elif opcao == "3":
        remover_livro()

    elif opcao == "4":
        atualizar_livro()

    elif opcao == "5":
        break

    else:
        print("Opção inválida. Tente novamente.")