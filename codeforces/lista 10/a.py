def contaVenda(estoque, pedidos):
    vendidos = 0

    for tamanho in pedidos:
        if estoque[tamanho - 1] > 0:
            estoque[tamanho - 1] -= 1
            vendidos += 1

    return vendidos


n = int(input())

estoque = []
for i in range(n):
    estoque.append(int(input()))

P = int(input())

pedidos = []
for i in range(P):
    pedidos.append(int(input()))

resultado = contaVenda(estoque, pedidos)


print(resultado)
