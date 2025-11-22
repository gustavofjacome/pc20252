def comb(n,k):
    if n==k:
        return 1
    
    if k==1:
        return n
    
    if 1<=k<=n:
        return comb(n-1, k-1) + comb(n-1, k)

x, y = map(int, input().split())   
print(comb(x,y))