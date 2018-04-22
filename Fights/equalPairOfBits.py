def equalPairOfBits(n, m):
    i = 1
    while (n & 1) != (m & 1):
        n >>= 1
        m >>= 1
        i <<= 1
    return i
#...........
def equalPairOfBits(n, m):
    x = bin(n)[2:][::-1]
    y = bin(m)[2:][::-1]

    for i in range(min(len(x), len(y))):
        if x[i] ==  y[i]:
            return 2 ** i
    return 2 ** (i+1)
