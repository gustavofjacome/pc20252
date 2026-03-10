n = int(input())
fita = list(map(int, input().split()))

distancia = [0] * n

contador = n  

# normal de 0 até n
for i in range(n):
    if fita[i] == 0:
        contador = 0
    else:
        contador += 1
    distancia[i] = contador

contador = n  # reset

# invertido de n até 0
for i in range(n - 1, -1, -1):
    if fita[i] == 0:
        contador = 0
    else:
        contador += 1
        distancia[i] = min(distancia[i], contador)

# 9 tons
for i in range(n):
    if distancia[i] > 9:
        distancia[i] = 9

print(*distancia)
