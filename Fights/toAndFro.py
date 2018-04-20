def toAndFro(a, b, t):

    length = abs(b - a)
    t %= 2 * length
    if t <= length:
        return a + (b - a) / abs(b - a) * t
    else:
        return b + (a - a) / abs(b - a) * (t-length)
