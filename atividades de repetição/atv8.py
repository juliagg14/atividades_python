salario_inicial= float(input("digite salario inicial"))
aumento= 0.015
ano_atual= 2023


for ano in range (ano_atual - 1996):
    aumento *= 2
    salario_atual= salario_inicial + salario_inicial * aumento

print("o salario do funcionario e: {:.2f}".format (salario_atual))


