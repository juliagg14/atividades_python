menu = '''candidatos
--------------------------------
1- yuri
2- julia
3- joão
4- matheus
5- nulo
6- branco
digite "S" para sair'''
print (menu)

yuri = 0 
julia = 0
joao = 0
matheus = 0
nulo = 0
brancos = 0


numnero_de_pessoas_para_votar = int (input("quantas pessoas vão votar: "))

for i in range ( numnero_de_pessoas_para_votar):
    votos = input("em quem deseja votar: " ).upper().strip()

    if votos =="1":
        yuri +=1
    elif votos == "2":
        julia += 1
    elif votos =="3":
        joao +=1
    elif votos =="4":
        matheus +=1
    elif votos =="5":
        nulo +=1
    elif votos =="6":
        brancos +=1
    

porcentagem_nulos= float(( nulo /numnero_de_pessoas_para_votar)*100)
porcentagem_brancos = float((brancos /numnero_de_pessoas_para_votar )*100)


print("yuri recebeu : ", yuri , "votos")
print("julia recebeu : ", julia , "votos")
print("joao recebeu : ", joao , "votos")
print("matheus recebeu : ", matheus , "votos")
print("tiveram: ", nulo , "votos nulos")
print("tiveram: ", brancos , "votos brancos")

print("a porcentagem de votos nulos foram de: ", porcentagem_nulos, "%")
print("a porcentagem de votos em branco foi de: ", porcentagem_brancos, "%")



