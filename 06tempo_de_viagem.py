tempo = 60
distancia = float(input("Qual a distância que será percorrida em km: "))
velocidadeMedia = int(input("Qual será a velocidade média durante o trajeto em km/h? "))

def duracaoViagem(tempo, distancia, velocidadeMedia):
    hora = distancia / velocidadeMedia

    tempoFinal = tempo * hora
    if tempoFinal < 60:
        return(f"tempo levado para completar essa trajetória será de: {tempoFinal:.2f} minutos")
    elif tempoFinal >= 60:
        return(f"O tempo levado para completar essa trajetória será de: {tempoFinal/60} horas")

print(duracaoViagem(60, distancia, velocidadeMedia))