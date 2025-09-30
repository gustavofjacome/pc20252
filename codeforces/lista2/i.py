L, D = map(int, input().split())
K, P = map(int, input().split())

custo_km = L * K
numeroPedagio = L // D
custoPedagios = numeroPedagio * P

print(custo_km + custoPedagios)
