caso = 1

while True:
    try:
        line = input()
        if not line:
            break
        n = int(line)

        oleos = list(map(float, input().split()))

        senha = ""

        for k in range(n):
            maior_oleo = -1.0
            posicao_escolhida = -1


            for i in range(10):
                if oleos[i] > maior_oleo:
                    maior_oleo = oleos[i]
                    posicao_escolhida = i

            senha += str(posicao_escolhida)

            oleos[posicao_escolhida] = -1.0

        print(f"Caso {caso}: {senha}")
        caso += 1

    except EOFError:
        break