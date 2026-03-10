while True:
    try:
        linha = input()
        dados = linha.split()

        n = int(dados[0])
        sequencia = []

        for i in range(1, n + 1):
            sequencia.append(int(dados[i]))

        if n == 1:
            print("Alegre")
            continue

        diferencas = []
        alegre = True

        for i in range(1, n):
            diferenca = abs(sequencia[i] - sequencia[i - 1])

            if diferenca < 1 or diferenca > n - 1:
                alegre = False
                break

            if diferenca in diferencas:
                alegre = False
                break

            diferencas.append(diferenca)

        if alegre:
            print("Alegre")
        else:
            print("Nao alegre")

    except EOFError:
        break
