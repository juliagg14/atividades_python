materias = int(input("quantas notas voce quer calcular a media?"))

lista_materias = []

for i in range (materias):
    
     notas = float(input("coloque as  notas das materias:"))
     lista_materias.append(notas)
     if notas == "":
           print("coloque as notas")
           continue
       
print("Suas notas foram: {}".format(lista_materias))

media = sum(lista_materias) / len(lista_materias)

print("a media de suas notas são de: {}".format(media))