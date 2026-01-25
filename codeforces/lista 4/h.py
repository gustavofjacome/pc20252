C = int(input())
A = int(input())

max_alunos = C - 1
viagens = A // max_alunos   

if A % max_alunos != 0:     
    viagens += 1 

print(viagens)
