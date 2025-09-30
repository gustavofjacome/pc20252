valorItem = int(input())
quantidadeItens = int(input())
quantidadeDinheiro = int(input())

valorPagar = valorItem*quantidadeItens


troco = quantidadeDinheiro - valorPagar

print(f'A pagar: {valorPagar}\n'
      f'Troco  : {troco}')