a, b = map(int, input().split())

sequenciaA = list(map(int, input().split()))
sequenciaB = list(map(int, input().split()))

verificador = 0  

for i in range(a):
    if verificador < b and sequenciaA[i] == sequenciaB[verificador]:
        verificador += 1

if verificador == b:
    print('S')
else:
    print('N')
