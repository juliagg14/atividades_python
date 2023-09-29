def converter_euro(reais):
    euro = 5.25
    valor = reais / euro
    return valor

def converter_dolar(reais):
    dolar = 4.97
    valor = reais / dolar
    return valor

def converter_libras(reais):
    libra = 6.07
    valor= reais / libra
    return libra


reais= float(input("quantos reais voce quer converter: "))

print( "1- dolar")
print("2- euro")
print("3- libra")

escolha = input("escolha uma oque voce quer converter: ")

if escolha == "1":
    resultado = converter_dolar(reais)
    print(f"valor: ","{:.2f}".format(resultado))

elif escolha == "2":
    resultado = converter_euro(reais)
    print(f"valor: "," {:.2f}".format(resultado))
    
elif escolha == "3":
    resultado = converter_libras(reais)
    print (f"valor "," {:.2f}".format(resultado))
    
else:
    print("opção invalida")