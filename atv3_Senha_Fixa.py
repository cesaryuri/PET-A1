conferencia = True
while(conferencia):
    senha = 2002
    senhain = int(input("Digite a senha: "))
    if(senha == senhain):
        print("Senha correta!")
        conferencia = False
    else:
        print("Senha incorreta!")