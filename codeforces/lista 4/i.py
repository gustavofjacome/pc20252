a, b, c = map(int, input().split())

#acho que tambem daria certo usando o sorted()
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b



if a + b <= c:
    print('n')


    
else:

    if a**2 + b**2 == c**2:
        print('r')  # retângulo
    elif a**2 + b**2 > c**2:
        print('a')  # acutângulo
    else:
        print('o')  # obtusângulo