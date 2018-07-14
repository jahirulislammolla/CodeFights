def specialPolynomial(x, n):
    c=0
    for i in  range(1000):
        c+=x**i
        if c>n:
            return i-1
        
