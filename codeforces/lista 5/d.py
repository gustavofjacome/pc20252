m = int(input())
a = int(input())
b = int(input())

c = m - (a + b) #idade do terceito filho
 
mais_velho = a

if b > mais_velho:
    mais_velho = b

if c > mais_velho:
    mais_velho = c

print(mais_velho)