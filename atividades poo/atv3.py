class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"Desculpe, o livro '{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido com sucesso.")
        else:
            print(f"Este livro já está disponível na biblioteca.")


livro1 = Livro("O poder da esperança", "Michelson Borges", 2018)
livro2 = Livro("Virando o jogo", "J. Sterling", 2000)
livro3 = Livro("O tipo certo de garota errada", "A. C. Meyer", 2018)


livro1.emprestar()
livro2.emprestar()
livro1.devolver()
livro3.emprestar()

print(f"Status de disponibilidade do livro 1: {livro1.disponivel}")
print(f"Status de disponibilidade do livro 2: {livro2.disponivel}")
print(f"Status de disponibilidade do livro 3: {livro3.disponivel}")