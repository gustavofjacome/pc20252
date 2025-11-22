def conta_bits(n):
    n = abs(n)  
    if n < 2: #binario = 2
        return 1
    else:
        return 1 + conta_bits(n // 2) #binario = 2

x = int(input())
print(conta_bits(x)) 