n = int(input())


#constantes -> tamanho do tabuleiro
LINHAS = 10
COLUNAS = 10

# 10x10 prenchido com 0
tabuleiro = []
for i in range(LINHAS):
    linha = []
    for j in range(COLUNAS):
        linha.append(0)
    tabuleiro.append(linha)

valido = True

for i in range(n):
    D, L, R, C = map(int, input().split())

    # converter para índice 0
    R -= 1
    C -= 1

    if D == 0:
        #sera que sai do tabuleiro
        if C + L > COLUNAS:
            valido = False
            break

        # sera que vai colidir com outro barco, considerei os espaços vazios como 0 e sempre que tem um barco vira 1 entao se ja tiver 1 é pq ja tem um barco lá
        for j in range(C, C + L):
            if tabuleiro[R][j] == 1:
                valido = False
                break

        if not valido:
            break

        # muda o local de onde o navio ta para 1 para sabermos onde ele está
        for j in range(C, C + L):
            tabuleiro[R][j] = 1

    else:  # vertical
        # ja foi explicado
        if R + L > LINHAS:
            valido = False
            break

        # ja foi explicado
        for i in range(R, R + L):
            if tabuleiro[i][C] == 1:
                valido = False
                break

        if not valido:
            break

        # ja foi explicado
        for i in range(R, R + L):
            tabuleiro[i][C] = 1



#for r in range(LINHAS):
#    for c in range(COLUNAS):
#        print(tabuleiro[r][c], end=' ')
#    print()




if valido:
    print("Y")
else:
    print("N")
