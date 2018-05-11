def create2DArray(lengths):
    x=[]
    for i in lengths:
        y=[]
        for j in range(i):
            y.append(j)
        x.append(y)
    return x
