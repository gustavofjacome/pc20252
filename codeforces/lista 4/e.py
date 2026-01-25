L = int(input())
C = int(input())

linha_impar = (L % 2 == 1)
coluna_impar = (C % 2 == 1)

if linha_impar == coluna_impar:
    print(1)  # branca
else:
    print(0)  # preta