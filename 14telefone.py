minuto = int(input("Quantos minutos você ficou em chamada? "))
if minuto < 200:
    print(f"O valor da sua conta é de R${minuto*0.20:.2f}")

elif minuto >= 200 and minuto <= 400:
    print(f"O valor da sua cobrança é de R${minuto*0.18:.2f}")

elif minuto > 400 and minuto <= 800:
    print(f"O valor da sua cobrança é de R${minuto*0.15:.2f}")

elif minuto > 800:
    print(f"O valor da sua cobrança é de R${minuto*0.08:.2f}")