def lista_troca_menor_primeiro(lista):
    posicaoMenorValor = lista.index(min(lista))

    if posicaoMenorValor != 0:
        lista[0], lista[posicaoMenorValor] = lista[posicaoMenorValor], lista[0]
        return 1 
    else:
        return 0 
