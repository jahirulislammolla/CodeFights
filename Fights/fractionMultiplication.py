from fractions import gcd
def fractionMultiplication(a, b):
    x=a[0]*b[0]
    y=a[1]*b[1]
    d=gcd(x,y)
    return [x//d,y//d]
