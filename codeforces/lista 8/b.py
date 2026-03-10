entrada = input().split()
s = int(entrada[0])
mi = int(entrada[1])

tempo_total = 0
massa = float(mi)

while massa >= 0.5:
    massa = massa / 2
    tempo_total = tempo_total + s

dias = tempo_total // 86400
tempo_total = tempo_total % 86400

horas = tempo_total // 3600
tempo_total = tempo_total % 3600

minutos = tempo_total // 60
segundos = tempo_total % 60

print(f"{dias} dias {horas:02d}:{minutos:02d}:{segundos:02d}")