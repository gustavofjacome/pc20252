n = int(input())
k = int(input())

notas = []
for i in range(n):
    notas.append(int(input()))

notas.sort(reverse=True)

classificados = k

while classificados < n and notas[classificados] == notas[classificados - 1]:
    classificados += 1

print(classificados)