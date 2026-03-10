def func2 ( l01 , num ):
    q = 0
    for i in range (1 , len ( l01 )):
        for j in range (0 , i):
            if l01 [i] + l01 [j] == num :
                q = q + 1
    return q


n = int ( input () )
lista = list ( map ( int , input () . split () ))
print ( func2 ( lista , n))