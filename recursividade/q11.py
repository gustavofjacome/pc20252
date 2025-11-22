# é primo?
def primo(n):
    if n <= 1:
        return False
    return eh_primo_rec(n, 2)
# auxixliar
def eh_primo_rec(n, div):
    if div * div > n:
        return True
    if n % div == 0:
        return False
    return eh_primo_rec(n, div + 1)

def primos(lista):
    if len(lista) == 0:
        return []
    
    primeiro = lista[0]
    
    if primo(primeiro):
        return [primeiro] + primos(lista[1:])
    else:
        return primos(lista[1:])

lista = list(map(int, input().split()))

x = primos(lista)
print(x)
