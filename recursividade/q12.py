def ocorrencias(lista, x):
    if len(lista) == 0:
        return 0
    
    primeiro = lista[0]

    if primeiro == x:
        return 1 + ocorrencias(lista[1:], x)
    else:
        return ocorrencias(lista[1:], x)


lista = list(map(int, input().split()))
valor = int(input())

x = ocorrencias(lista, valor)
print(x)
