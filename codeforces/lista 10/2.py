n, p = map(int, input().split())

contador = 0

for i in range(n):
    x, y = map(int, input().split())

    if x+y >= p:
        contador += 1


print(contador)