tempo = 60
distancia = float(input("Qual a distância que será percorrida em km: "))
velocidadeMedia = int(input("Qual será a velocidade média durante o trajeto em km/h? "))

hora = distancia / velocidadeMedia

tempoFinal = tempo * hora
if tempoFinal < 60:
    print(f"tempo levado para completar essa trajetória será de: {tempoFinal:.2f} minutos")
elif tempoFinal >= 60:
    print(f"O tempo levado para completar essa trajetória será de: {tempoFinal/60} horas")
