dias = int(input("Digite a quantidade em dias: "))
horas = int(input("Digite a quantidade em horas: "))
minutos = int(input("Digite a quantidade em minutos: "))

segundos = (minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

print(segundos)