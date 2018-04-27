def uniqueDigitProducts(a):
    x=[]
    for i in a:
        b=1
        for j in map(int,list(str(i))):
            b*=j
        x.append((b))
    return len(set(x))
