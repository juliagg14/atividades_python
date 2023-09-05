cobertura_por_litro = 3

tamanho_da_lata = 18


preco_por_lata = 80.00


area_a_ser_pintada = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))


litros_de_tinta_necessarios = area_a_ser_pintada / cobertura_por_litro

latas_de_tinta_necessarias = int(litros_de_tinta_necessarios / tamanho_da_lata) + 1


preco_total = latas_de_tinta_necessarias * preco_por_lata


print("Quantidade de latas de tinta necessárias: ", latas_de_tinta_necessarias)
print("Preço total: R$", preco_total)
