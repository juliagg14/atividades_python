preco_alcool = 1.90
preco_gasolina = 2.50


litros_vendidos = float(input("Informe o número de litros vendidos: "))
tipo_combustivel = input("Informe o tipo de combustível (A para álcool, G para gasolina): ").strip().upper()


if tipo_combustivel == "A": # ALCOOL
    if litros_vendidos <= 20:
        valor_a_pagar = litros_vendidos * (preco_alcool - (preco_alcool * 0.03))


    else:
        valor_a_pagar = litros_vendidos * (preco_alcool - (preco_alcool * 0.05))
elif tipo_combustivel == "G": #GASOLINA
    if litros_vendidos <= 20:
        valor_a_pagar = litros_vendidos * (preco_gasolina - (preco_gasolina * 0.04))

        
    else:
        valor_a_pagar = litros_vendidos * (preco_gasolina - (preco_gasolina * 0.06))
else:
    print("Tipo de combustível inválido. Use 'A' para álcool ou 'G' para gasolina.")
    valor_a_pagar = 0


if valor_a_pagar > 0:
    print("Total a pagar: R$", valor_a_pagar)





