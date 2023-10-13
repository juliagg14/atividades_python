gerenciador_de_produtos = {}

 

def adicionar_produto(nome,preco,quantidade):

    gerenciador_de_produtos[nome] = {

        "preco": preco,

        "quantidade": quantidade

    }

   

   

def remover_produto(nome):

    del gerenciador_de_produtos[nome]

       

 

def obter_produto(nome):

    return gerenciador_de_produtos.get(nome)

 

def atualizar_produto(nome,preco,quantidade):

    if nome in gerenciador_de_produtos:

        gerenciador_de_produtos[nome]['preco'] = preco

        gerenciador_de_produtos[nome]['quantidade'] = quantidade

       

 

def exibir_produtos():

    for nome, dados in gerenciador_de_produtos.items():

        print(f"nome: {nome}")

        print(f"preco: {dados['preco']}")

        print(f"quantidade: {dados['quantidade']}")

        print()

 

print("1- adicionar")

print("2- remover")

print("3- atualizar")

print("4- exibir")

print("5- sair")

 

 

 

while True:

    opcao = input("digite o numero da opcao: ")

 

    if opcao == '1':

        nome = input("digite o nome do produto que deseja adicionar: ")

        preco = float(input("digite o preco do produto que deseja adicionar: "))

        quantidade = int(input("digite a quantidade do produto que deseja adicionar: "))

        adicionar_produto(nome,preco,quantidade)

        exibir_produtos()

   

    elif opcao == '2':

        exibir_produtos()

        nome = input("digite o nome do produto que deseja remover: ")

        remover_produto(nome)

        exibir_produtos()

       

   

    elif opcao == '3':

        nome = input("digite o nome do produto que deseja atualizar: ")

        preco = float(input("digite o novo preco do produto que deseja atualizar: "))

        quantidade = int(input("digite a nova quantidade do produto que deseja atualizar: "))

        atualizar_produto(nome,preco,quantidade)

        exibir_produtos()

   

    elif opcao == '4':

        exibir_produtos()

   

    elif opcao == '5':

        break    