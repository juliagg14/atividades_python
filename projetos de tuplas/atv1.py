produtos = []
precos = []
quantidades = []


while True:
    produto = input("nome do produto: (press 's' para sair)").strip()


    if produto == 's':
        print("não tem mais nada para adicionar")
        break


    quantidade = int(input("Quantas unidades? (press '0' para sair)"))

    if quantidade == 0:
        print("não tem mais nada para adicionar")
        break



    preco = float(input("quanto custa esse produto?"))
    produto_tuple = (produto, preco, quantidade)
    produtos.append(produto_tuple)
    print("---------------------------------------------------------")

 

print("1- Atualizar preco e quantidade")
print("2- Remover preco e quantidade")
print("3- Não tenho nada para Atualizar/Remover")

opcao = int(input("Qual opcao deseja realizar?"))

if opcao == 1:
    nome_produto = input("Qual produto deseja atualizar?").strip()
    novo_preco = float(input("Digite o novo preco:"))
    nova_quantidade = int(input("Digite a nova quantidade:"))


    for i in range(len(produtos)):
        if produtos[i][0] == nome_produto:
            produtos[i] = (nome_produto, novo_preco, nova_quantidade)
            break


elif opcao == 2:
    nome_produto = input("Qual produto deseja remover?").strip()


    for i in range(len(produtos)):
        if produtos[i][0] == nome_produto:
            del produtos[i]
            break


for produto in produtos:
    print("---------------------------------------------------------")
    print(produto[0], "-", "R$", produto[1])
    print("quantidade do produto em estoque:", produto[2])
    print("---------------------------------------------------------")

