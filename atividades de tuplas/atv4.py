valor1 = int(input("coloque o primeiro valor: "))
valor2 = int (input("coloque o segundo valor: "))

auxiliar = 0

lista1 = [(valor1, valor2)]

print("estes são os valores que voce colocou antes", lista1)

auxiliar = valor1
valor1 = valor2

numeros_trocados = [valor1, auxiliar]

print(f"agora a nova ordem e {numeros_trocados}")