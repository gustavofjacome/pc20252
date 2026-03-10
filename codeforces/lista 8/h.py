while True:
    n = int(input())
    if n == 0:
        break
    
    h = list(map(int, input().split()))
    
    picos = 0
    
    for i in range(n):
        anterior = h[(i - 1 + n) % n]
        atual = h[i]
        proximo = h[(i + 1) % n]
        
        if atual > anterior and atual > proximo:
            picos += 1
            
        elif atual < anterior and atual < proximo:
            picos += 1
    
    print(picos)