from Crypto.Util.number import inverse

P = (2339, 2213)
Q = P
n = 7863
R = (0, 0)


def pt_add(p, q, E):
    zero = (0, 0)
    if p == zero:
        return q
    elif q == zero:
        return p
    else:
        x1, y1 = p
        x2, y2 = q
        if x1 == x2 and y1 == -y2:
            return zero

        Ea, Ep = E['a'], E['p']
        if p != q:
            lmd = (y2 - y1) * inverse(x2 - x1, Ep)
        else:
            lmd = (3 * (x1**2) + Ea) * inverse(2 * y1, Ep)
        x3 = ((lmd**2) - x1 - x2) % Ep
        y3 = (lmd * (x1 - x3) - y1) % Ep
        return x3, y3


E = {'a': 497, 'b': 1768, 'p': 9739}

while n > 0:
    if n % 2 == 1:
        if R == (0, 0):
            R = Q
        else:
            R = pt_add(R, Q, E)
    Q = pt_add(Q, Q, E)
    n = n // 2
print(R)
