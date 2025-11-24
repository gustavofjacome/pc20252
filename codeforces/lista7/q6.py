def ehprimo(x):
    listaDivisores = []
    for i in range(1, x+1):
        if x % i == 0:
            listaDivisores.append(i)

    if len(listaDivisores) == 2:
        return "Sim"
    else:
        return "Nao"


a = int(input())
print(ehprimo(a))
