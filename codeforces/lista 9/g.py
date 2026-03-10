while True:
    entrada = input()
    
    if entrada == '*':
        break
    
    palavras = entrada.split()
    letra_inicial = palavras[0][0].lower()
    
    e_tautograma = True
    
    for palavra in palavras:
        if palavra[0].lower() != letra_inicial:
            e_tautograma = False
            break
            
    if e_tautograma:
        print('Y')
    else:
        print('N')