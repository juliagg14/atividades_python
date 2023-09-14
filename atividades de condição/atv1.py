peso_peixe = float (input("informe o peso(kg): "))
peso_max = 50.0


if (peso_peixe > peso_max):
   excesso = peso_peixe - peso_max


   multa =  excesso * 4.0

   print("O excesso de peso foi de:  " , + excesso , "kg")
   print("A multa sera de : R$",  + multa)

else:
   print("não excedeu os limites então não pagara multa")
