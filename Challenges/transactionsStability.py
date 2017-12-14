def transactionsStability(t):
    t=sorted(set(t))
    l=len(t)
    if l==1:
        return 1
    x,j,e=0,l-1,0
    for i in range(l-1):
        a=max(t[j-1], t[l-1] / 2)
        b=min(t[0], t[j] / 2)
        x=b/a
        if x<=e:
            break
        e=x
        j-=1
    return e
