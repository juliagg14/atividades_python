portugues = float(input("coloque a sua nota de portugues: "))
ingles= float(input("coloque a sua nota de ingles: "))
matematica = float (input("coloque a sua nota de matematica: ")) 
fisica = float(input("coloque a sua nota de fisica: "))
biologia = float(input("coloque a sua nota de biologia: "))

nota = [portugues, ingles, matematica, fisica, biologia]
media = [(portugues + ingles + matematica + fisica + biologia) / (len(nota))]
print(media)