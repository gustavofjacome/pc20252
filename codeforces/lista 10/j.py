n = int(input())
listaDesequilibrada = list(map(int, input().split()))

n = len(listaDesequilibrada)        # número de degraus
S = sum(listaDesequilibrada)        # total de blocos

x = (S - n*(n-1)//2) / n  # menor degrau possível

print(x)