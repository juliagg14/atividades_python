lista = []

while True:
    numeros = input("coloque uma lista de numeros. (ou precione 's' para sair)").lower()
    if numeros == 's':
        break


    try:
        numero_int = int(numeros)
        lista.append(numero_int)

    except:
        print("valos invalido")    

escolha = input("quer uma ordem crescente ou decrescente  (c/d)").lower()

if escolha == 'c':
    lista.sort()
    print(lista)


elif escolha == 'd':
    lista.sort(reverse=True)
    print(lista)