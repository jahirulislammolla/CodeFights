def summaryProficiency(a, n, m):
    x=0
    for i in a:
        if n>0 and i>=m:
            x+=i
            n-=1
    return x
