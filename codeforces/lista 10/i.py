n = int(input())

sequenciaN = list(map(int, input().split()))
sequenciaDiff = []



for i in range (n - 1):
    sequenciaDiff.append(sequenciaN[i] - sequenciaN[i+1])


total = len(set(sequenciaDiff)) 

print(total)