#Escreva uma função, em Python, que receba 3 números inteiros e retorne True se o maior for
#múltiplo do menor, e False caso contrário.

def multiplo_do_menor(a, b, c):
    maior = a
    if b>a and b>c:
        maior = b
    if c>b and c>a:
        maior = c

    menor = a
    if b<a and b<c:
        menor = b
    if c<b and c<a:
        menor = c

    if maior%menor == 0:
        return True
    else:
        return False
    


x = int(input())
y = int(input())
z = int(input())

print(multiplo_do_menor(x,y,z))
