pais_A = 80000
taxa_crescimento_A= 0.03

pais_B = 200000
taxa_crescimento_B = 0.015
ano= 0 
while pais_A < pais_B :
 pais_A += pais_A * taxa_crescimento_A
 pais_B+= pais_B * taxa_crescimento_B
 ano += 1


print("a população do pais 'A' ultrapassou a população do pais 'B' em", ano , "anos")