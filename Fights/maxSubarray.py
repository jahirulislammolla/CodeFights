def maxSubarray(inputArray):
    s=0
    d=0
    for i in inputArray:
        if s+i>=i:
            s+=i
            if s>d:
                d=s
        else:
            s=max(0,i)
    return d
