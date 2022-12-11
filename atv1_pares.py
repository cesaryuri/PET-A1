contador = 0
for i in range (1,6):
    int1 = int(input(f"Digite um núnero {i}º:"))   
    if (int1 % 2) == 0:
        contador += 1

print(f"O número de valores pares é: {contador}")