T = int(input())
 
for _ in range(T):
    D, N = map(float, input().split())
    prices = list(map(float, input().split()))
 
    best = 0.0
 
    for p in prices:
        k = int(D // p)   
        if k >= 1:
            change = D - k * p
            if change > best:
                best = change
 
    print(f"{best:.2f}")