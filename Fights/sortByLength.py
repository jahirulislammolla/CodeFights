def sortByLength(inputArray):
    x={}
    for i in inputArray:
        if len(i) not in x:
            x[len(i)]=[]
        x[len(i)]+=[i]
    y=[]
    for i in sorted(x):
        for j in x[i]:
            y.append(j)
    return y
