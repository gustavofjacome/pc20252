def g( l01 ):
    if len ( l01 ) == 0:
        return 10
    else :
        n = l01 [ -1]
        if n % 2 == 1:
            return 1 + g( l01 [: -1])
        else:
            return 10 * g( l01 [: -1])




lista = list ( map ( int , input () . split () ))
lista . append ( len ( lista ))
lista . append (2)
print (g( lista ))