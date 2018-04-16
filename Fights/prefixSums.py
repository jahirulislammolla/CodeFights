def prefixSums(a):
    s=0
    y=[]
    for i in a:
        y.append(s+i)
        s+=i
    return y
