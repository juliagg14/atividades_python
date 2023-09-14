cardapio = {
    100 :{'item': 'cachorro quente', 'preco': 1.20},
    101: {'item': 'bauru simples', 'preco': 1.30},
    102: {'item': 'bauru com ovo', 'preco': 1.50},
    103: {'item': 'hamburguer', 'preco': 1.20},
    104: {'item': 'cheeserbuguer', 'preco': 1.30},
    105: {'item': 'refrigerante', 'preco': 1.00}
}
geral = 0

while True:
    codigo1 = int (input("digite o codigo o primeiro item (ou 0 para encerrar):"))
    if codigo1 == 0:
        break

    quantidade1 = int(input("digite a quantidade desejada para o primeiro item: "))

    if codigo1 in cardapio:
        item1 = cardapio[codigo1]
        valor_item1 = item1['preco'] * quantidade1
        geral += valor_item1

        print(f"item: {item1['item']}")
        print(f"valor a ser pago por item : R${valor_item1:.2f}\n")

    else:
        print("codigo invalido. tente Novamente.\n")
        continue

    segunda_ordem = input("deseja fazer seu segundo pedido ? (sim/nao):")
    if segunda_ordem.lower() == "nao":
        break


    codigo2 = int(input("digite o codigo do segundo item"))
    quantidade2 = int(input("digite a quantidade desejada para o segundo item: "))
    
    if codigo2 in cardapio:
        item2 = cardapio[codigo2]
        valor_item2 = item2['preco'] * quantidade2
        geral += valor_item2

        print(f"item: {item2['item']}")
        print(f"valor a ser pago por item: R${valor_item2:.2}\n")

    else:
        print("codigo invalido. tente novamente. \n")
        continue
    print(f"total geral do pedido : R$ {geral:.2f}")