n = int(input())

texto = input()

total_as_validos = 0
conta_atual = 0

for letra in texto:
    if letra == 'a':
        conta_atual += 1
    else:
        if conta_atual >= 2:
            total_as_validos += conta_atual
  
        conta_atual = 0


if conta_atual >= 2:
    total_as_validos += conta_atual

print(total_as_validos)