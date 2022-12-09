def valorPagamento(valorpres , numdiatr):
    if(numdiatr > 0):
        valorpresj = 0
        valorpresj += valorpres * 0.03
        valorpresj += (valorpres * (0.001 * numdiatr))
        valorpres += valorpresj
    return valorpres

totalpagamen = 0
contador = 0
while (True):
    valorpres = float(input("Digite o valor da prestação: "))
    
    if(int(valorpres) == 0): 
        break

    contador += 1
    numdiatr= int(input("Digite o número de dias em atraso: "))
    print(f"O valor da prestação é : {valorPagamento(valorpres , numdiatr)}")
    totalpagamen += valorPagamento(valorpres , numdiatr)
    
print(f"O valor total das prestações é: {totalpagamen} sendo pago um total de {contador} prestações")