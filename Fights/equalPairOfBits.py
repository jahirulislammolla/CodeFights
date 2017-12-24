def equalPairOfBits(n, m):
    r=1
    c=0
    while n and m:
        if n%2==m%2:
            return 2**c
        c+=1
        n//=2
        m//=2
    return r
    #return n + m + 1 & ~m - n
