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

# Cria a janela
window = tk.Tk()
window.title("Calculadora de Multa por Excesso de Peso de Peixe")
window.geometry("400x200")
window.configure(bg="purple")


peso_label = tk.Label(window, text="Informe o peso do peixe (kg):")
peso_label.pack(pady=10)

entry_peso = tk.Entry(window)
entry_peso.pack()

# botão 
calcular_button = tk.Button(window, text="Calcular Multa", command=calcular_multa)
calcular_button.pack()


resultado_label = tk.Label(window, text="")
resultado_label.pack(pady=10)

# Inicia a janela
window.mainloop()