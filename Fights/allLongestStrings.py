def allLongestStrings(inputArray):
    x={}
    for i in inputArray:
        l=len(i) 
        if l not in x:
            x[l]=[]
        x[l]+=[i]
    return x[max(x)]
