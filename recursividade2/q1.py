def soma_alg(n):
    if (n == 0):
        return 0
    else:
        return n + soma_alg(n-1)
    
print(soma_alg(6))