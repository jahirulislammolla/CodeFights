def swapNeighbouringDigits(n):
    x=list(str(n))
    y=''
    for i in range(0,len(x),2):
        y+=x[i+1]+x[i]
    return y
    
    
