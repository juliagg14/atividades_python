# Inicializa um dicionário vazio para armazenar as tarefas
tarefas = {}

# Função para adicionar uma tarefa à lista
def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas[tarefa] = False  # False indica que a tarefa não foi concluída

# Função para listar as tarefas
def listar_tarefas():
    print("Lista de tarefas:")
    for tarefa, concluida in tarefas.items():
        status = "Concluída" if concluida else "Não Concluída"
        print(f"- {tarefa} ({status})")

# Função para marcar uma tarefa como concluída
def marcar_tarefa_concluida():
    tarefa = input("Digite a tarefa que deseja marcar como concluída: ")
    if tarefa in tarefas:
        tarefas[tarefa] = True
        print(f"A tarefa '{tarefa}' foi marcada como concluída.")
    else:
        print(f"A tarefa '{tarefa}' não foi encontrada na lista.")

# Loop principal do programa
while True:
   menu = '''("\nOpções:")
   ("1. Adicionar tarefa")
   ("2. Listar tarefas")
   ("3. Marcar tarefa como concluída")
   ("4. Sair")'''
   print(menu)
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        marcar_tarefa_concluida()
    elif opcao == "4":
        break  # Sai do programa
    else:
        print("Opção inválida. Por favor, digite um número válido.")