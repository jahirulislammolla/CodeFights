def checkEqualFrequency(inputArray):
    x={}
    for i in inputArray:
        if i not in x:
            x[i]=0
        x[i]+=1
    d=x[inputArray[-1]]
    for i in x:
        if x[i]!=d:
            return 0
    return 1
