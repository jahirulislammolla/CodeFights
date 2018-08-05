def magicalWell(a, b, n):
    s=0
    while n>0:
        s+=a*b
        a+=1
        b+=1
        n-=1
    return s
