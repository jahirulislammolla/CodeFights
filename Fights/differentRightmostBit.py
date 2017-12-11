def differentRightmostBit(n, m):
    return 2**math.log2((m^n) & -(m^n))
