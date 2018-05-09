# - Suppose the following
#     f = x^0 + x^1 + x^2 + x^3 + x^4 + x^5 + x^6 + x^7
#     n = 5
# - The fifth derivative is
#     0 +
#     0 +
#     0 +
#     0 +
#     0 +
#     (5*4*3*2*1)x^0 +
#     (6*5*4*3*2)x^1 + 
#     (7*6*5*4*3)x^2 +
# - The first n coefficients get annihilated
# - The first scalar (for x^0) is always factorial(n)
# - The next scalars can be calculated by multiplying
#   by n+1 and dividing by 1, then multiplying by n+2
#   and dividing by 2, and so on
# - Since the first n coefficients are ignored, we can
#   use the n iterations to accumulate the factorial

c, n, x = eval(dir()[0])
t = 0
i = p = 1
for v in c:
    p *= i
    if i > n:
        t += p/i*v
        p *= x
        p /= i-n
    i += 1
    
return t % (10**9 + 7)

#my solution not pass all test case time limit
def nthDerivative(co, n, m):
    x=[1]
    c=1
    d=0
    p=1000000007
    j=0
    k=0
    for i in range(1,len(co)):
        c=c*i
        x+=[c]
        if i>n:
            k+=pow(co[i]*c//x[i-n]*m**i,1,p)
    return k%1000000007
