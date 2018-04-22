def maxDivisor(left, right, divisor):
    m=right
    while m>=left:
        if m%divisor==0:
            return m
        m-=1
    return -1
