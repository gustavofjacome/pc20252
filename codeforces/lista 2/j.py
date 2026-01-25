L = int(input())
C = int(input())

totalTipo1 = (L*C) + (L-1) * (C-1)

totalTipo2 = (L - 1) * 2 + (C - 1) * 2

print(f'{totalTipo1}\n'
      f'{totalTipo2}')