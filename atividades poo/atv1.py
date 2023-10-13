class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade Atual: {self.velocidade} km/h")


marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = int(input("Digite o ano de fabricação do carro: "))


meu_carro = Carro(marca, modelo, ano)

while True:
    print("\nEscolha uma opção:")
    print("1 - Acelerar")
    print("2 - Frear")
    print("3 - Exibir informações do carro")
    print("4 - Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        incremento = int(input("Digite a quantidade para acelerar (em km/h): "))
        meu_carro.acelerar(incremento)
    elif escolha == "2":
        decremento = int(input("Digite a quantidade para frear (em km/h): "))
        meu_carro.frear(decremento)
    elif escolha == "3":
        meu_carro.informacoes()
    elif escolha == "4":
        print("Saindo do programa. Obrigado!")
        break
