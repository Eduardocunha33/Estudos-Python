salario_atual = float(input("Digite o salário atual: "))
porcentagem = int(input("Digide a porcentagem de aumento salarial: "))

calculo_por = porcentagem / 100 
calculo_sal = salario_atual * calculo_por + salario_atual

print(f"O salário atual com o reajuste será de: R${calculo_sal:.2f}")