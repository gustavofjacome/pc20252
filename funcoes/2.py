#Escreva uma função, em Python, que receba 4 números inteiros e retorne a soma dos dois menores.

def soma_dois_menores(n1, n2, n3, n4):
    lista = [n1,n2,n3,n4]
    lista_ordenada = sorted(lista)

    return lista_ordenada[0] + lista_ordenada[1]


a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(soma_dois_menores(a,b,c,d))