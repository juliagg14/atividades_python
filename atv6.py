numero1= int (input("digite o primeiro numero: "))
numero2= int(input("digite o segundo numero: "))

operacao = input("qual operacao deseja fazer:  +  , - , * , / : ")


if operacao == "+": 
   resultado = numero1 + numero2
   print("O Resultado é: ", resultado)

elif operacao == "-":
   resultado = numero1 - numero2
   print("O Resultado é: ", resultado)

elif operacao == "*":
   resultado == numero1 * numero2
   print("O Resultado é: ", resultado)

elif operacao == "/":
   resultado == numero1 / numero2
   print("O Resultado é: ", resultado)

else: 
   print("coloque algo")


if resultado < 0:
  print("esse numero e negativo")
else:
   print("esse numero e positivo")

if "." in str  (resultado):
   print ("o numero e decimal")

if resultado % 2 == 0: 
   print ("numero par")
else:
   print ("numero impar")