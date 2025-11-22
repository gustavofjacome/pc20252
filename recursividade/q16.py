def junta(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1

    ultimo1 = l1[-1]
    ultimo2 = l2[-1]

    if ultimo1 > ultimo2:
        return junta(l1[:-1], l2) + [ultimo1]
    else:
        return junta(l1, l2[:-1]) + [ultimo2]