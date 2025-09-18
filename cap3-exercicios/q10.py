valor_item, quantidade, valor_pago = map(int, input("Digite o valor do item, a quantidade e quanto você tem: ").split())

total = valor_item * quantidade
troco = valor_pago - total


print("A pagar:", total)
print("Troco:", troco)