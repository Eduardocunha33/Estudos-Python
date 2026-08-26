valor_produto = float(input("Digite o valor da compra: "))
desconto_compra = int(input("Digite a porcentam em desconto: "))

porcentagem = desconto_compra / 100
valor_com_desconto = valor_produto * porcentagem
valor_final = valor_produto - valor_com_desconto
print(f"O valor da compra era R${valor_produto} recebeu {desconto_compra}% de desconto({valor_com_desconto}) preço total a se pago: R${valor_final}")