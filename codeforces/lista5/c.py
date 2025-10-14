a = int(input())
b = int(input())
c = int(input())

#carro B precisa ser acelerado se (B−A) < (C−B),  
#desacelerado se (B−A) > (C−B)
#e manter a velocidade se (B−A) for igual a (C−B)
# dava para usar elif mas quis fazer diferente
if (b-a < c-b):
    print('1')

else:
    if (b-a > c-b):
        print('-1')
    else:
        if (b-a == c-b):
            print('0')