*X, n = eval(dir()[0])
N = numpy

A, B, C = [N.reshape([*map(ord,x)], (n,n)) for x in X]

e = 0
for i in '       ':
    r = N.random.randint(0,2,n)
    e |= 1 in A@(B@r)-C@r&1
return 1-e

#...................
*a,N = eval(dir()[0])
d,e,f = [[[*map(ord,z[i*N:-~i*N])] for i in range(N)] for z in a]
r = numpy.array([1,1,0,0,1,N<11]*N)[:N]
#for _ in "        ":
#    r = numpy.random.randint(2,size=N)
#    if any(d @ (e @ r) & 1 != f @ r & 1):
#        return 0
return any(d @ (e @ r) - f @ r & 1) < 1
#.........................
import numpy as N, random as R

def matrixCheck(a, b, c, n):
    a,b,c= ['1'==N.reshape(N.array([x for x in A]),(n,n)) for A in [a,b,c]]
    t=1
    for _ in '       ':
        v=N.array(R.sample(range(999),n))%2
        if (a @ (b @ v)%2 != c @ v % 2).any(): t=0
    return t
#...................
# https://en.wikipedia.org/wiki/Freivalds%27_algorithm

from numpy import reshape, dot
a, b, c, n = eval(dir()[0])
toMatrix = lambda s: reshape(map(ord,s), (n,n))
A = toMatrix(a)
B = toMatrix(b)
C = toMatrix(c)

for _ in xrange(5):
    r = [random.random() < 0.5 for _ in xrange(n)]
    if not all(dot(A, dot(B, r)) % 2 == dot(C, r) % 2):
        return 0
return 1
