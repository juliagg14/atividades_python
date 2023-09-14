quantidade_morangos = float(input("Quantos quilos de morangos você deseja comprar? "))
quantidade_macas = float(input("Quantos quilos de maçãs você deseja comprar? "))


preco_morangos = 2.50 if quantidade_morangos <= 5 else 2.20


preco_macas = 1.80 if quantidade_macas <= 5 else 1.50


valor_total = (quantidade_morangos * preco_morangos) + (quantidade_macas * preco_macas)


if (quantidade_morangos + quantidade_macas) > 8 or valor_total > 25.00:
    valor_total *= 0.90 


print("Valor total a ser pago: R$", valor_total)