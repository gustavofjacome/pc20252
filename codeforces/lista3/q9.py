diametro = int(input())
a, l, p = map(int, input().split())


if (a>=diametro and l>=diametro and p>=diametro):
    print('S')

else:
    print('N')