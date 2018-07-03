def launchSequenceChecker(systemNames, stepNumbers):
    x={}
    for i,j in zip(systemNames,stepNumbers):
        if i not in x:
            x[i]=[]
        x[i]+=[j]
    for i in x:
        if x[i]!=sorted(x[i]) or len(set(x[i]))!=len(x[i]):
            return 0
    return 1
