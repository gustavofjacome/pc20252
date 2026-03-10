n = int(input())
batimentos = []

for i in range(n):
    batimentos.append(int(input()))

media = sum(batimentos) // n

limite_inferior = int(media * 0.9)
limite_superior = int(media * 1.1)

fora_do_padrao = 0

for b in batimentos:

    if b < limite_inferior or b > limite_superior:
        fora_do_padrao += 1

print(media)
print(fora_do_padrao)