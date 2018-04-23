def polynomialMinimum(coeffs, interval):
    def f(x):
        res = 0
        for c in coeffs:
            res = res*x + c 
        return res

    l, r = interval[0], interval[1]

    while r - l >= 3:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        if f(m1) > f(m2):
            l = m1
        else:
            r = m2

    res = f(l)
    while l <= r:
        if f(l) < res:
            res = f(l)
        l += 1

    return res
