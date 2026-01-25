A, B, C = map(int, input().split())


if A == 0 or B == 0 or C == 0:
    print("S")


elif A + B == 0 or A - B == 0 or B - A == 0 or A + C == 0 or A - C == 0 or C - A == 0 or B + C == 0 or B - C == 0 or C - B == 0:
    print("S")


elif A + B + C == 0 or A + B - C == 0 or A - B + C == 0 or -A + B + C == 0 or A - B - C == 0 or -A + B - C == 0 or -A - B + C == 0 or -A - B - C == 0:
    print("S")
else:
    print("N")
