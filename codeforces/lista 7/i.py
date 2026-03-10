n = int(input())
ganhou = 0

for i in range(n):
    porta_carro = int(input())
    if porta_carro != 1:
        ganhou += 1

print(ganhou)
