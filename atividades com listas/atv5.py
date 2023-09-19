notas = []
valor = 0 

while valor != -1:
    valor = float(input("infome uma nota (-1 para encerrar):"))
    if valor != -1:
        notas.append(valor)


quantidades_notas = len(notas)


print(" valores informqados:")

for nota in notas:
    print(nota, end="")

print ("\nValores na ordem inversa:")
for nota in reversed(notas):
    print (nota)


soma = sum(notas)
print(f"soma dos valores:{soma}")

media = soma/ quantidades_notas
print(f"media dos valores: {media:.2f}")


acima_da_media = sum(1 for nota in notas if nota > media)

abaixo_de_sete = sum (1 for nota in notas if nota < 7)

print (f"quantidade de valores acima da media: {acima_da_media}")
print(f"quantidade de valores abaixo de sete : { abaixo_de_sete}")

print("programa encerrado.")