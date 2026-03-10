while True:
    H1, M1, H2, M2 = map(int, input().split())
    
    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break
    
    dormiu = H1 * 60 + M1
    acordou = H2 * 60 + M2
    
    if acordou >= dormiu:
        print(acordou - dormiu)
    else:
        print((24 * 60 - dormiu) + acordou)
