sequenciaDNA = input().strip()

maximo = 1
atual = 1

for i in range(1, len(sequenciaDNA)):
    if sequenciaDNA[i] == sequenciaDNA[i - 1]:
        atual += 1
        
        if atual > maximo:
            maximo = atual
    else:
        atual = 1

print(maximo)
