A = int(input())
B = int(input())
C = int(input())
D = int(input())

diferenca_1 = (A + B) - (C + D)
if diferenca_1 < 0:
    diferenca_1 = -diferenca_1  

diferenca_2 = (A + C) - (B + D)
if diferenca_2 < 0:
    diferenca_2 = -diferenca_2

diferenca_3 = (A + D) - (B + C)
if diferenca_3 < 0:
    diferenca_3 = -diferenca_3

menor = diferenca_1

if diferenca_2 < menor:
    menor = diferenca_2

if diferenca_3 < menor:
    menor = diferenca_3

print(menor)
