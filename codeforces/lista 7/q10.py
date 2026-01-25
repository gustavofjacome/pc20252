n = int(input())

seq = []
for i in range(n):
    seq.append(int(input()))

cont = 1

for i in range(1, n):
    if seq[i] != seq[i-1]:
        cont += 1

print(cont)
