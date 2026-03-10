def mediaLista(a, lista):
    a = int(input())
    lista = list(map(int, input().split()))
    media = sum(lista) / len(lista)

    abaixoMedia = 0
    acimaMedia = 0

    for i in range(len(lista)):
        if lista[i] < media:
            abaixoMedia += 1
        else:
            acimaMedia += 1

    return media, abaixoMedia, acimaMedia


media, abaixo, acima = mediaLista(0, [])
print(f"{media:.1f}")
print(abaixo)
print(acima)
