def lastDigit(a, b):
    m=1
    for i in range(1,b+1):
        m*=a
        m%=10
    return m
