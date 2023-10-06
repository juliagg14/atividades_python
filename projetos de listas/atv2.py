tarefas = []
opcao = ""


while opcao != "s":

    print("1- Adicionar tarefa")
    print("2- Remover tarefa")
    print("3- Listar tarefa")
    print("Digite 's' para encerrar o programa. ")

    opcao = input("O que você gostaria de fazer?")

    if opcao == "1":
        tarefa = input("Digite a tarefa que deseja adicionar:")
        tarefas.append(tarefa)
        print("-----------------------------")
        print("tarefa adicionada")
        print("-----------------------------")


    elif opcao == "2":
        tarefa = input("Digite a tarefa que deseja remover:")

        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("-----------------------------")
            print("tarefa removida")
            print("-----------------------------")

        else:
            print("-----------------------------")
            print("essa tarefa não está na lista")
            print("-----------------------------") 

    elif opcao == "3":

        if tarefas:
            print("-----------------------------")
            print("tarefas a fazer:")
            for tarefa in tarefas:
                print("-" + tarefa)
            print("-----------------------------")        

        else:
            print("a lista está vazia")

    elif opcao == "s":
        print("programa encerrado")
        break        