from fractions import gcd
def fractionSum(a, b):
    x=a[0]*b[1]+a[1]*b[0]
    y=a[1]*b[1]
    g=gcd(x,y)
    return [x//g,y//g]
