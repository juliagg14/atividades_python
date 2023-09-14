respostas_positivas = 0


print("Responda 'Sim' ou 'Não' para as seguintes perguntas:")

if input("Telefonou para a vítima? ").strip().lower() == "sim":
    respostas_positivas += 1

if input("Esteve no local do crime? ").strip().lower() == "sim":
    respostas_positivas += 1

if input("Mora perto da vítima? ").strip().lower() == "sim":
    respostas_positivas += 1

if input("Devia para a vítima? ").strip().lower() == "sim":
    respostas_positivas += 1

if input("Já trabalhou com a vítima? ").strip().lower() == "sim":
    respostas_positivas += 1


if respostas_positivas == 2:
    print("Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")