import gmpy2
a = 497
b = 1768
p = 9739
P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)


def add(l, x1, x2, y1):
    x3 = (l**2 - x1 - x2) % p
    y3 = ((l * (x1 - x3)) - y1) % p
    return x3, y3


l = (3 * P[0]**2 + a) * int(gmpy2.invert(2*P[1], p))
tmp = add(l, P[0], P[0], P[1])
print(tmp)
l = (Q[1] - tmp[1]) * gmpy2.invert(Q[0] - tmp[0], p)
tmp = add(l, tmp[0], Q[0], tmp[1])
print(tmp)
l = (R[1] - tmp[1]) * gmpy2.invert(R[0] - tmp[0], p)
tmp = add(l, tmp[0], R[0], tmp[1])
print(tmp)
