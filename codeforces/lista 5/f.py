ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())

nao_recebe = 0

if cr > ca:
    nao_recebe = nao_recebe + (cr - ca)

if br > ba:
    nao_recebe = nao_recebe + (br - ba)

if pr > pa:
    nao_recebe = nao_recebe + (pr - pa) 

print(nao_recebe)
