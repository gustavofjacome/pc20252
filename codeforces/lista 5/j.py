#      w1        w2
#   +---------+---------+
#   |         |         |
# h1|   A     |   B     |
#   |         |         |
#   +---------+---------+
#   |         |         |
# h2|   C     |   D     |
#   |         |         |
#   +---------+---------+

A, B, C, D = map(int, input().split())

if A * D == B * C or A * B == C * D or A * C == B * D or B * C == A * D or B * D == A * C or C * D == A * B:
    print('S')
else:
    print('N')
