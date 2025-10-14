c = int(input())
d = int(input())
t = int(input())

autonomiaAtual = c * t

distanciaQueSeraPercorrida = d - autonomiaAtual

seraAbastecido = distanciaQueSeraPercorrida / c

if seraAbastecido < 0:
    seraAbastecido = 0

print(f'{seraAbastecido:.1f}')