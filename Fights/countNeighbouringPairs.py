def countNeighbouringPairs(s):
    x=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            x+=1
    return x
