import tkinter as tk

# Lista de tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa:
        tarefas.append(tarefa)
        tarefa_adicionada_label.config(text="Tarefa adicionada: " + tarefa)
        entry_tarefa.delete(0, tk.END)
        listar_tarefas()
    else:
        tarefa_adicionada_label.config(text="Por favor, digite uma tarefa.")

# Função para remover uma tarefa
def remover_tarefa():
    tarefa = entry_remover.get()
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        tarefa_removida_label.config(text="Tarefa removida: " + tarefa)
        entry_remover.delete(0, tk.END)
        listar_tarefas()
    else:
        tarefa_removida_label.config(text="Essa tarefa não está na lista.")

# Função para listar as tarefas
def listar_tarefas():
    lista_tarefas_text.config(state=tk.NORMAL)
    lista_tarefas_text.delete(1.0, tk.END)

    if tarefas:
        for idx, tarefa in enumerate(tarefas, start=1):
            lista_tarefas_text.insert(tk.END, f"{idx}. {tarefa}\n")
    else:
        lista_tarefas_text.insert(tk.END, "A lista está vazia.")

    lista_tarefas_text.config(state=tk.DISABLED)

# Criar janela
window = tk.Tk()
window.title("Gerenciador de Tarefas")
window.geometry("400x400")
window.configure(bg="purple")

# Rótulo e entrada para adicionar tarefa
adicionar_label = tk.Label(window, text="Adicionar Tarefa:", bg="purple", fg="white")
adicionar_label.pack(pady=5)

entry_tarefa = tk.Entry(window)
entry_tarefa.pack()

adicionar_button = tk.Button(window, text="Adicionar", command=adicionar_tarefa, bg="purple", fg="white")
adicionar_button.pack(pady=5)

tarefa_adicionada_label = tk.Label(window, text="", bg="purple", fg="white")
tarefa_adicionada_label.pack()

# Rótulo e entrada para remover tarefa
remover_label = tk.Label(window, text="Remover Tarefa:", bg="purple", fg="white")
remover_label.pack(pady=5)

entry_remover = tk.Entry(window)
entry_remover.pack()

remover_button = tk.Button(window, text="Remover", command=remover_tarefa, bg="purple", fg="white")
remover_button.pack(pady=5)

tarefa_removida_label = tk.Label(window, text="", bg="purple", fg="white")
tarefa_removida_label.pack()

# Rótulo e área de texto para listar as tarefas
listar_label = tk.Label(window, text="Listar Tarefas:", bg="purple", fg="white")
listar_label.pack(pady=5)

lista_tarefas_text = tk.Text(window, height=10, width=30)
lista_tarefas_text.config(state=tk.DISABLED)
lista_tarefas_text.pack()


# Iniciar a interface
window.mainloop()