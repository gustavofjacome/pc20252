c = int(input())
saldo = 100
max_premio = saldo

for i in range(c):
    v = int(input())
    saldo += v
    if saldo > max_premio:
        max_premio = saldo

print(max_premio)
