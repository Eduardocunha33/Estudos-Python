cigarro_dia = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Qual a quantidade de anos que você fuma? "))

reducaoMinuto = cigarro_dia * 10
reducaoAno = anos * 365
totalMinPerdido = (reducaoMinuto * reducaoAno) * 10
diasPminutos = 24 * 60

print(f"Você perdeu: {(totalMinPerdido/diasPminutos)/10:.2f} dias de vida.")