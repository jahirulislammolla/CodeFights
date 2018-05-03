def splitByValue(k, elements):
    x=[]
    y=[]
    for i in elements:
        if i<k:
            x.append(i)
        else:
            y.append(i)
    return x+y
