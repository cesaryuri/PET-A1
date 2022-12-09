while(True):
  senhain = int(input("Digite um valor para a lista: "))
  
  if(senhain < 0):
        break
  lista = []
  lista.append(senhain)     

media = (sum(lista))/(len(lista))
print(f"A média dos valores listados é: {media}")