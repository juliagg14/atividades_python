vetorUm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetorDois= [11, 12, 13, 14, 15, 16 ,17, 18, 19 ,20]
vetorTres= [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
vetor_intercalado = []



valor = min(len(vetorUm), len(vetorDois), len(vetorTres))

for i in range (valor):
 vetor_intercalado.append(vetorUm[i])
 vetor_intercalado.append(vetorDois[i])
 vetor_intercalado.append(vetorTres[i])
 
print (vetor_intercalado)

