seg = int(input("Digite o tempo em segundos: "))

h = seg // 3600
m = (seg % 3600) // 60
s = seg % 60

print(h, "h", m, "m", s, "s")
