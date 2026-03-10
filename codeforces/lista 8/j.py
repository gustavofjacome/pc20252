linha = input().split()
N = int(linha[0])
R = int(linha[1])

retornaram = list(map(int, input().split()))

marcou = []
for i in range(N + 1):
    marcou.append(False)

for x in retornaram:
    marcou[x] = True

faltaram = []
for i in range(1, N + 1):
    if not marcou[i]:
        faltaram.append(i)

if len(faltaram) == 0:
    print("*")
else:
    saida = ""
    for x in faltaram:
        saida += str(x) + " "
    print(saida)
