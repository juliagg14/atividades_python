import random

class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.experiencia = 0

    def atacar(self, alvo):
        dano = random.randint(5, 15)
        alvo.vida -= dano
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")

    def usar_item(self, item):
        if item == "poção":
            cura = random.randint(10, 20)
            self.vida += cura
            print(f"{self.nome} usou uma poção e recuperou {cura} de vida.")

    def ganhar_experiencia(self, quantidade):
        self.experiencia += quantidade
        print(f"{self.nome} ganhou {quantidade} de experiência.")

    def __str__(self):
        return f"{self.nome} ({self.classe}): Vida = {self.vida}, Experiência = {self.experiencia}"

class Monstro:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 50

    def atacar(self, alvo):
        dano = random.randint(8, 12)
        alvo.vida -= dano
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")

    def __str__(self):
        return f"{self.nome}: Vida = {self.vida}"

# Função para iniciar uma batalha entre o personagem e um monstro
def batalha(personagem, monstro):
    print(f"{personagem.nome} enfrenta um {monstro.nome}!")

    while personagem.vida > 0 and monstro.vida > 0:
        escolha = input("Escolha uma ação (atacar/usar_item): ").lower()

        if escolha == "atacar":
            personagem.atacar(monstro)
            if monstro.vida <= 0:
                print(f"{personagem.nome} derrotou o {monstro.nome}!")
                personagem.ganhar_experiencia(20)
        elif escolha == "usar_item":
            personagem.usar_item("poção")
        else:
            print("Escolha uma ação válida.")

        if monstro.vida > 0:
            monstro.atacar(personagem)
            if personagem.vida <= 0:
                print(f"{personagem.nome} foi derrotado pelo {monstro.nome}. Fim de jogo!")

# Exemplo de uso do jogo RPG com interatividade
nome_personagem = input("Digite o nome do seu personagem: ")
classe_personagem = input("Escolha a classe do seu personagem (Guerreiro/Mago): ").capitalize()

personagem = Personagem(nome_personagem, classe_personagem)
monstro = Monstro("Dragão")

print(f"Você é {personagem.nome}, um(a) {personagem.classe}.")

while personagem.vida > 0:
    batalha(personagem, monstro)
    continuar = input("Deseja continuar jogando? (sim/não): ").lower()
    if continuar != "sim":
        break

print("O jogo terminou. Até a próxima!")