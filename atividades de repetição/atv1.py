usuario= input("coloque seu usuario: ").upper().strip()
senha= input("informe sua senha ").upper().strip()

while usuario == senha:
    print ("coloque uma diferente do seu nome de usuario")
    break