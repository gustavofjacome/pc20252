teste = 1
while True:
    entrada = input().split()
    
    if not entrada:
        break
        
    n = int(entrada[0])
    
    if n == 0:
        break
    
    primeira_regiao = list(map(int, input().split()))
    x_res = primeira_regiao[0]
    y_res = primeira_regiao[1]
    u_res = primeira_regiao[2]
    v_res = primeira_regiao[3]
    
    for i in range(n - 1):
        regiao = list(map(int, input().split()))
        x = regiao[0]
        y = regiao[1]
        u = regiao[2]
        v = regiao[3]
        
        if x > x_res:
            x_res = x
        if y < y_res:
            y_res = y
        if u < u_res:
            u_res = u
        if v > v_res:
            v_res = v
            
    print(f"Teste {teste}")
    
    if x_res < u_res and v_res < y_res:
        print(f"{x_res} {y_res} {u_res} {v_res}")
    else:
        print("nenhum")
        
    print()
    teste += 1