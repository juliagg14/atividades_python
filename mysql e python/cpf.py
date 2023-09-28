def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = 0
    peso = 10
    
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    digito_1 = (soma * 10) % 11
    if digito_1 == 10:
        digito_1 = 0

    if int(cpf[9]) != digito_1:
        return False

    soma = 0
    peso = 11

    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
    digito_2 = (soma * 10) % 11

    if digito_2 == 10:
        digito_2 = 0

    if int(cpf[10]) != digito_2:
        return False
    return True

cpf = input("Digite o CPF: ")
if validar_cpf(cpf):
    print("CPF válido")

else:
    print("CPF inválido")