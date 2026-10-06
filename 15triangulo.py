a = float(input("Digite o valor de um dos lados do triângulo: "))
b = float(input("Digite o valor de outro lado do triângulo: "))
c = float(input("Digite o valor do terceiro lado do triângulo: "))

if a > b + c or b >a + c or c > a + b:
    print("Não é possível formar um triângulo com esses valores.")
else:
    if a == b and b == c:
        print("O triangulo é Equilátero. Todos os lados são iguais.")
    elif a == b or b == c or a == c:
        print("O triangulo é Isósceles. Pelo menos dois lados possuem a mesma medida.")
    else:
        print("O triangulo é Escaleno. Pois todos os lados possuem medidas diferentes.")