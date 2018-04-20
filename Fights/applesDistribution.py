def applesDistribution(apples, boxCapacity, maxResidue):
    res=0
    for i in range(1,boxCapacity+1):
        if apples%i<=maxResidue:
            res+=1
    return res
