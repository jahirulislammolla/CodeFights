def digitDistanceNumber(n):
    y=[]
    x=list(str(n))
    for i in range(len(x)-1):
        y.append(str(abs(int(x[i])-int(x[i+1]))))
    return itn"".join(y)
