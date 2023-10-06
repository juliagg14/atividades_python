import tkinter as tk

def calcular_salario():
    salario_inicial = float(entry_salario_inicial.get())
    aumento = 0.015
    ano_atual = 2023

    for _ in range(ano_atual - 1996):
        aumento *= 2
        salario_inicial += salario_inicial * aumento

    resultado_label.config(text=f"O salário do funcionário é: R$ {salario_inicial:.2f}")

# Criar janela
window = tk.Tk()
window.title("Cálculo de Salário com Aumento Anual")
window.geometry("400x200")
window.configure(bg="purple")

# Rótulo e entrada para o salário inicial
salario_label = tk.Label(window, text="Digite o salário inicial:", bg="purple", fg="white")
salario_label.pack(pady=10)

entry_salario_inicial = tk.Entry(window)
entry_salario_inicial.pack()

# Botão para calcular o salário
calcular_button = tk.Button(window, text="Calcular Salário", command=calcular_salario, bg="purple", fg="white")
calcular_button.pack()

# Rótulo para exibir o resultado
resultado_label = tk.Label(window, text="", bg="purple", fg="white")
resultado_label.pack(pady=10)

# Iniciar a interface
window.mainloop()
