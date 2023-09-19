total_gasto_abonos = 0 
numeros_funcionarios_minimo = 0
maior_abono = 0
resultados = []



while True:
    salario = float(input("Salario ( digite 0 para encerrar):"))
    if salario == 0:
        break
    
    
    abono = max(salario * 0.2, 100)
    
    if abono > maior_abono:
        maior_abono = 1
        
    
    if abono == 100:
        numeros_funcionarios_minimo += 1
        
    
    resultados.append((salario, abono))
    total_gasto_abonos += abono
    
    for salario, abono in resultados:
        print (f"Salarios: R$ {salario:.2f} - abono: R$ {abono:.2f}")
        
        
        
print("\n Foram processados", len(resultados), "colaboradores")
print("Total gasto com abonos: R${:.2f}".format(maior_abono))
print("Valor minimo pago a", numeros_funcionarios_minimo, "colaboradores")
print("Maior valor de abono pago: R${:.2f}".format(maior_abono)) 
    