def climbingStairs(n):
    b=f(n+1)  
    return b[0]
    x=[-1]*n
    def f(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = f(n // 2)
            c = (a * (2 * b - a))%(10**9+7)
            d = (b * b + a * a)%(10**9+7)

            if n % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)
#..................
def climbingStairs(n):
    a=b=1
    while n:
        a,b=b,a+b
        n-=1
    return a
