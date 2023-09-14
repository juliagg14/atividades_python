tabela_de_precos = {}


for produto in range(1,51):
    preco = produto * 1.99
    tabela_de_precos[produto] = preco



print("lojas quase dois - tabela de preço")

for produto, preco in tabela_de_precos.items():
    print(produto,  "- R$", preco)
