def reduzir(texto_numero):
    while len(texto_numero) > 1:
        lista_digitos = [int(d) for d in texto_numero]
        soma = sum(lista_digitos)
        texto_numero = str(soma)
    return int(texto_numero)

while True:
    linha = input().split()
    
    if not linha:
        break
        
    n = linha[0]
    m = linha[1]

    if n == '0' and m == '0':
        break

    res_n = reduzir(n)
    res_m = reduzir(m)

    if res_n > res_m:
        print(1)
    elif res_m > res_n:
        print(2)
    else:
        print(0)