def indice_do_maior(lista):
    if len(lista) == 1: # se um elemento
        return 0
    if lista[-1] == max(lista): #se ultimo maior
        return len(lista) - 1
    else:
        return indice_do_maior(lista[:-1]) #remove ultimo e chama dnv
    
x = list(map(int, input().split()))
print(indice_do_maior(x))
