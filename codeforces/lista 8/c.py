P, N = map(int, input().split())
canos = list(map(int, input().split()))

venceu = True

for i in range(N - 1):
    if abs(canos[i] - canos[i + 1]) > P:
        venceu = False
        break

if venceu:
    print("YOU WIN")
else:
    print("GAME OVER")
