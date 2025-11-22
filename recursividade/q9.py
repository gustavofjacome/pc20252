def soma_pares(lista):
    if len(lista) == 0:
        return 0
    
    primeiro = lista[0]
    
    if primeiro % 2 == 0:
        return primeiro + soma_pares(lista[1:])
    else:
        return soma_pares(lista[1:])

lista = list(map(int, input().split()))

x = soma_pares(lista)
print(x)
