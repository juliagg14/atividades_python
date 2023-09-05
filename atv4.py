import math


cobertura_por_litro = 6


tamanho_lata_18_litros = 18
tamanho_galao_3_6_litros = 3.6

preco_lata_18_litros = 80.00
preco_galao_3_6_litros = 25.00


area_a_ser_pintada = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))


area_a_ser_pintada *= 1.1


litros_de_tinta_necessarios = area_a_ser_pintada / cobertura_por_litro


latas_de_18_litros_necessarias = math.ceil(litros_de_tinta_necessarios / tamanho_lata_18_litros)


galoes_de_3_6_litros_necessarios = math.ceil(litros_de_tinta_necessarios / tamanho_galao_3_6_litros)


latas_minimas = math.floor(litros_de_tinta_necessarios / tamanho_lata_18_litros)
litros_restantes = litros_de_tinta_necessarios - (latas_minimas * tamanho_lata_18_litros)
galoes_minimos = math.ceil(litros_restantes / tamanho_galao_3_6_litros)


preco_total_latas = latas_de_18_litros_necessarias * preco_lata_18_litros
preco_total_galoes = galoes_de_3_6_litros_necessarios * preco_galao_3_6_litros
preco_total_combinacao = (latas_minimas * preco_lata_18_litros) + (galoes_minimos * preco_galao_3_6_litros)


print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas necessárias: ", latas_de_18_litros_necessarias)
print("Preço total: R$", preco_total_latas)

print("\nSituação 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões necessários: ", galoes_de_3_6_litros_necessarios)
print("Preço total: R$", preco_total_galoes)

print("\nSituação 3: Misturar latas e galões (minimizando desperdício)")
print("Quantidade de latas necessárias:", latas_minimas)
print("Quantidade de galões necessários:", galoes_minimos)
print(f"Preço total: R$", preco_total_combinacao)









