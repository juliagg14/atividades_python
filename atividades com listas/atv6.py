menu = '''Vote no sistema operacional que voce mais gosta.
     para finalizar o programa e so digitar ( 0 )
     
para votar basta digitar os numeros abaixo de acordo com qual sitema voce quer votar.
1 - windows server.
2 - unix.
3 - linux.
4 - netware.
5 - mac os.
6 - outro.
'''
print (menu)



votos  = [0, 0, 0, 0, 0, 0]

total_votos = 0 

while True: 
        print("escolha o sistema operacional (1 - windows server, 2 - unix, 3 - linux, 4 - netware, 5- mac os, 6- outro): ")
        voto = int(input())
        
        if voto < 0 or voto > 6:
          print("voto invalido. pr favor, insira  um valor entre 1 e 6.")
          continue

        if voto == 0:
         break


        votos[voto -1] += 1
        total_votos += 1 


print ("\n sistema operacional votos    %")
print("----------------------------------")


sistemas_operacionais = ["Windows server","unix", "linux", "netware", "mac os", "outros"]
vencedor = ""
mais_votos = 0

for i in range(6):
     percentual = (votos[i] / total_votos) * 100
     print( f"{sistemas_operacionais[i]:<20}{votos[i]:<6} {percentual:.2f}%")
     
     if votos[i] > mais_votos:
        mais_votos = votos[i]
        vencedor = sistemas_operacionais[i]

print("----------------------------------")

print(f"total                  {total_votos}\n")


print(f"o sistema operacional mais votado foi o {vencedor}, com {mais_votos} votos, corre4spondendo a {((mais_votos / total_votos) * 100):.2f}% dos votos.")  