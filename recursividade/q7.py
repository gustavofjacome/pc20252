#Escreva uma função recursiva que receba um número inteiro n e retorne uma lista com os divisores de n.
#Assinatura da função: def divisores(n,k)

def divisores(n,k):
    if  k>n:
        return []
    if n%k == 0:
        return [k] + divisores(n,k+1)
    else:
        return divisores(n,k+1)

x, y = map(int, input().split())   
print(divisores(x,y))