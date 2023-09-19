vetorUm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetorDois= [11, 12, 13, 14, 15, 16 ,17, 18, 19 ,20]
vetorTres= []

valor = min(len(vetorUm), len(vetorDois))

for i in range (valor):
 vetorTres.append(vetorUm[i])
 vetorTres.append(vetorDois[i])
 
print (vetorTres)