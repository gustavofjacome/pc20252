n = int(input())  

if n <= 10:
    conta = 7
elif n <= 30:
    conta = 7 + (n - 10) * 1
elif n <= 100:
    conta = 7 + 20 + (n - 30) * 2
else:
    conta = 7 + 20 + 70 * 2 + (n - 100) * 5

print(conta)
