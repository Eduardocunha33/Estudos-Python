dias = int(input("Quantos dias você alugou o carro? "))
km = float(input("Quantos quilômetros você rodou com o carro? "))

diaria = dias * 60
rodado = km * 0.15
print(f"O total ficou: R${diaria + rodado:.2f}")
