salario_horas = float (input("quanto você recebe por hora: "))
horas_trabalhadas = float(input("quantas horas você trabalha no mês: "))


salario_bruto = salario_horas * horas_trabalhadas

ir = (salario_bruto * 0.11) / 100 
inss = (salario_bruto * 0.8) / 100
sindicato = (salario_bruto * 0.5) / 100

descontos = ir + inss + sindicato

salario_liquido = salario_bruto - descontos


print("você recebe :", salario_bruto)
print("você pagou: R$", ir ,"de imposto de renda")
print("descontou para o INSS : R$", inss)
print("descontou para o sindicato R$", sindicato)
print("O seu salario liquido sera de: ", salario_liquido)