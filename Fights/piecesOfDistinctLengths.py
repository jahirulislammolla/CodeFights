def piecesOfDistinctLengths(strawLength):
    x=0
    c=0
    for i in range(1,strawLength+1):
        if x+i>strawLength:
            return c
        c+=1
        x+=i
        
