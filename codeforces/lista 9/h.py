n = int(input())
numeros = list(map(int, input().split()))

qtd_escadinhas = 1

for i in range(2, n):
    diferenca_atual = numeros[i] - numeros[i-1]
    diferenca_anterior = numeros[i-1] - numeros[i-2]
    
    if diferenca_atual != diferenca_anterior:
        qtd_escadinhas += 1

print(qtd_escadinhas)