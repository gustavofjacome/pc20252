n = int(input())
somatorio = 0

for i in range(0,n):
    somatorio += (1/(i+1))

print(f"{somatorio:.4f}")