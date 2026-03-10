n = int(input())
estadoInterruptor = list(map(int, input().split()))
a = False
b = False

for i in estadoInterruptor:
  if i == 1:
    a = not(a)

  if i == 2:
    a = not(a)
    b = not(b)

print(int(a))
print(int(b))