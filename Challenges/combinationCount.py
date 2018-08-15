def combinationCount(a,b,c):
    a.sort()
    b.sort()
    c.sort()
    j=k=0
    s=v=0
    xx={}
    yy={}
    l_a=len(a)
    l_b=len(b)
    l_c=len(c)
    t=1
    for i in range(l_a):
        m=a[i]
        while j<l_b and b[j]<=m:
            j+=1
        l=v
        if not t:
            try:
                v+=s-yy[j]
            except:
                v+=0
        if t:
            for p in range(j,l_b):
                n=b[p]
                yy[p]=s
                while k<l_c and c[k]<=n:
                    k+=1
                xx[p]=l_c-k
                s+=xx[p]
            t=0
            v=s
    return v
