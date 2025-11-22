def primo_aux(n, divisor):
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return primo_aux(n, divisor - 1)

def primo(n):
    if n < 2:
        return False
    return primo_aux(n, n - 1)

x = int(input())
print(primo(x))
