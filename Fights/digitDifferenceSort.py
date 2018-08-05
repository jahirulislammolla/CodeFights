def digitDifferenceSort(a):
    x={}
    y=[]
    for i in a:
        m=sorted(str(i))
        d=abs(int(m[0])-int(m[-1]))
        if d not in x:
            x[d]=[]
        x[d]+=[i]
    for i in sorted(x):
        y+=x[i][::-1]
    return y
