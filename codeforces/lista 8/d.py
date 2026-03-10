n = int(input())
candidato = n + 1
while True:
    eh_primo = True
    divisor = 2
    while divisor * divisor <= candidato:
        if candidato % divisor == 0:
            eh_primo = False
            break
        divisor = divisor + 1
    if eh_primo:
        print(candidato)
        break
    candidato = candidato + 1