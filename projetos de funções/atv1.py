def adicao (a,b):
    return a + b

def subtracao (a,b):
     return a - b
 
def multiplicacao (a,b):
     return a * b
 
def divisao (a,b):
    return a / b

menu = '''calculadora simples
1- adição
2- subtração
3- multiplicação
4- divisão'''

print(menu)

escolha =input("escolha uma das opções: ")

numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input("digite o segundo numero: "))

if escolha == "1":
    resultado = adicao(numero1,numero2)
    print (resultado)
    
elif escolha == "2":
    resultado = subtracao(numero1,numero2)
    print(resultado)
    
elif escolha =="3":
    resultado = multiplicacao(numero1,numero2)
    print(resultado)
    
elif escolha == "4":
    resultado = divisao(numero1,numero2)
    print(resultado)
    
else:
    print("opção invalida")