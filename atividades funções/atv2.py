numero1= int(input("digite um numero: "))

def verificar_par(numero1):
    if numero1 % 2 == 0:
        print("o numero e par")
        
    elif numero1 == 0 :
        print("ele e neutro")
         
    else:
        print(" o numero e impar")
    
verificar_par(numero1)