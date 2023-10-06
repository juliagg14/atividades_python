import tkinter as tk

def calcular_soma():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    soma = num1 + num2
    numeros.append((num1, num2))
    resultado_label.config(text=f"Numeros: {numeros}\nSoma: {soma}")

numeros = []


window = tk.Tk()
window.title("Cálculo de Soma de Números")
window.geometry("400x200")
window.configure(bg="gray")


num1_label = tk.Label(window, text="Digite o primeiro número:", bg="purple", fg="white")
num1_label.pack(pady=5)

entry_num1 = tk.Entry(window)
entry_num1.pack()


num2_label = tk.Label(window, text="Digite o segundo número:", bg="purple", fg="white")
num2_label.pack(pady=5)

entry_num2 = tk.Entry(window)
entry_num2.pack()

# botão para calcular 
calcular_button = tk.Button(window, text="Calcular Soma", command=calcular_soma, bg="purple", fg="white")
calcular_button.pack(pady=10)

# lista
resultado_label = tk.Label(window, text="", bg="white", fg="black")
resultado_label.pack()
window.mainloop()
