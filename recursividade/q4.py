def conta_algarismos(n):

    n = abs(n)  

    if n < 10:
        return 1
    else:
        return 1 + conta_algarismos(n // 10)

x = int(input())

print(conta_algarismos(x)) 