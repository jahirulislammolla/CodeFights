from fractions import gcd
def fractionSubtraction(a, b):
    x=a[0]*b[1]-b[0]*a[1]
    y=a[1]*b[1]
    m=gcd(x,y)
    return [x//m,y//m]

