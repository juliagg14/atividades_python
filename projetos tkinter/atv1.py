import tkinter as tk

def calcular_multa():
    peso_peixe = float(entry_peso.get())
    peso_max = 50.0

    if peso_peixe > peso_max:
        excesso = peso_peixe - peso_max
        multa = excesso * 4.0

        resultado_label.config(text=f"Excesso de peso: {excesso} kg\nMulta: R$ {multa:.2f}")
    else:
        resultado_label.config(text="Não excedeu os limites, não há multa.")

# Criar janela
window = tk.Tk()
window.title("Calculadora de Multa por Excesso de Peso de Peixe")
window.geometry("400x200")

# Rótulo e entrada para o peso do peixe
peso_label = tk.Label(window, text="Informe o peso do peixe (kg):")
peso_label.pack(pady=10)

entry_peso = tk.Entry(window)
entry_peso.pack()

# Botão para calcular multa
calcular_button = tk.Button(window, text="Calcular Multa", command=calcular_multa)
calcular_button.pack()

# Rótulo para exibir o resultado
resultado_label = tk.Label(window, text="")
resultado_label.pack(pady=10)

# Iniciar a interface
window.mainloop()