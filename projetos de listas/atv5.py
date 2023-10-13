produtos = []
precos = []

while True:
    produto = input("Produto: (ou precione 's' para sair)").lower()

    if produto == 's':
        break

    preco = float(input("Preço: "))
    produtos.append(produto)
    precos.append(preco)

 

print("-----------------------------------")

print("produtos dentro do carrinho:")

for i in range(len(produtos)):
    print(produtos[i],"-", precos[i], "R$")

print("-----------------------------------")

total = sum(precos)

print("O valor que você devera pagar é de: ", total, "R$")
print("---------------------------------------------------------")