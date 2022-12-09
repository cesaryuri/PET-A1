def calculasalario(salario):
    salario -= (salario*0.11)
    salario -= (salario*0.15)
    return salario

salario = float(input("Digite o valor do salário bruto: "))
print(f"Salário Líquido = R$ {calculasalario(salario)}")