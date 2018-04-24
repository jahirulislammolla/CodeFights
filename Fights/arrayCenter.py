def arrayCenter(a):
    avg = sum(a) / len(a)
    m = min(a)
    return [bi for bi in a if abs(bi - avg) < m]
