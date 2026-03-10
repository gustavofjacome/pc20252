mensagemCifrada = input()
cribs = input()

listaMensagemCifrada = list(mensagemCifrada)
listaCribs = list(cribs)

numerosDePosicaoDoCrib = 0
numeroDeVezesQueMoveParaDireita = len(listaMensagemCifrada) - len(listaCribs) + 1

for i in range(numeroDeVezesQueMoveParaDireita):
    posicaoValida = True
    for j in range(len(listaCribs)):
        if listaMensagemCifrada[i + j] == listaCribs[j]:
            posicaoValida = False
            break
    
    if posicaoValida:
        numerosDePosicaoDoCrib += 1

print(numerosDePosicaoDoCrib)