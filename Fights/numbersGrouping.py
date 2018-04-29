def numbersGrouping(a):
    x=[]
    for i in range(100000):
        x.append(0)
    for i in range(len(a)):
        d=(a[i]-1)//10000
        if x[d]==0:
            x[d]+=2
        else:
            x[d]+=1
    return sum(x)
