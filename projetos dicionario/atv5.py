def exibir_pergunta(pergunta, opcoes):
    print(pergunta)
    for i, opcao in enumerate(opcoes):
        print(f"{i+1}. {opcao}")

def verificar_resposta(resposta, opcao_correta):
    return resposta == opcao_correta

perguntas = [
    {
        "pergunta": "Quem pintou a obra 'A Noite Estrelada'?",
        "opcoes": ["Leonardo da Vinci", " Michelangelo", "Salvador Dalí", "Vincent van Gogh"],
        "opcao_correta": 4
    },
    {
        "pergunta": "Quem pintou a Mona Lisa?",
        "opcoes": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
        "opcao_correta": 1
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "opcoes": ["Júpiter", "Marte", "Vênus", "Saturno"],
        "opcao_correta": 1
    },
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["Paris", "Londres", "Berlin", "Roma"],
        "opcao_correta": 1
    }
]
pontuacao = 0
for pergunta in perguntas:
    exibir_pergunta(pergunta["pergunta"], pergunta["opcoes"])
    resposta = int(input("Digite o número da opção correta: "))
    if verificar_resposta(resposta, pergunta["opcao_correta"]):
        print("Resposta correta!")
        pontuacao += 1
        
    else:
        print("Resposta incorreta!")
print(f"Sua pontuação final: {pontuacao}/{len(perguntas)}")