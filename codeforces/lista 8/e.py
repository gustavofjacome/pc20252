N = int(input())

for i in range(N):
    C = float(input())
    dias = 0

    while C > 1.0:
        C /= 2.0
        dias += 1

    print(f"{dias} dias")
