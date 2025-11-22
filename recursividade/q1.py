def conta_divisores(n, div=None):
    if div is None:
        div = n
    if div == 1:
        return 1
    if n % div == 0:
        return 1 + conta_divisores(n, div - 1)
    else:
        return conta_divisores(n, div - 1)

x = int(input())
print(conta_divisores(x))
