
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


def positivo_ou_negativo(numero):
    if numero >= 0:
        return "positivo"
    else:
        return "negativo"


def inteiro_ou_decimal(numero):
    if numero.is_integer():
        return "inteiro"
    else:
        return "decimal"


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


operacao = input("Escolha a operação (soma, subtração, multiplicação, divisão): ")


if operacao == "soma":
    resultado = numero1 + numero2
elif operacao == "subtração":
    resultado = numero1 - numero2
elif operacao == "multiplicação":
    resultado = numero1 * numero2
elif operacao == "divisão":
    if numero2 == 0:
        print("Erro! Divisão por zero.")
        resultado = None
    else:
        resultado = numero1 / numero2
else:
    print("Operação inválida")
    resultado = None

if resultado is not None:
    print("Resultado da operação: ", resultado)
    print("O número " , resultado ,  " é ",  par_ou_impar(resultado), {positivo_ou_negativo(resultado)} , "e" , {inteiro_ou_decimal(resultado)})

