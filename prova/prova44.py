def f4 ( l01 , l02 ):
    ans = 0
    for i in range ( len ( l01 )):
        for j in range (i + 1, len ( l02 )):
            if l01 [i] == l02 [j ]:
                ans = ans + 1
                break
    return ans

lista1 = list ( map ( int , input () . split () ))
lista2 = list ( map ( int , input () . split () ))
print ( f4 ( lista1 , lista2 ))