n = int(input())
lista = list(map(int, input().split()))

media = sum(lista) / n

abaixo = []
acima = []

for i in range(len(lista)):
    if lista[i] < media:
        abaixo.append(lista[i])
    else:
        acima.append(lista[i])

print(f"{media:.1f}")
print(len(abaixo), *abaixo)
print(len(acima), *acima)
