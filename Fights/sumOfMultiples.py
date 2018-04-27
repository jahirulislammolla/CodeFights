def sumOfMultiples(n, k):
    s=0
    d=0
    while s+k<=n:
        s+=k
        d+=s
    return d
