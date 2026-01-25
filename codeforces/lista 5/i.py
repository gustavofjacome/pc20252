a1 = int(input())
a2 = int(input())
a3 = int(input())
# tem q contar o tempo de ida e de volta
custo_andar1 = (a2 * 2) + (a3 * 4)
custo_andar2 = (a1 * 2) + (a3 * 2)
custo_andar3 = (a1 * 4) + (a2 * 2)

menor_tempo = custo_andar1

if custo_andar2 < menor_tempo:
  menor_tempo = custo_andar2

if custo_andar3 < menor_tempo:
  menor_tempo = custo_andar3

print(menor_tempo)