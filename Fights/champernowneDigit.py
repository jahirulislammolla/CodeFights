def champernowneDigit(n):
    x=""
    for i in range(1,n+1):
        x+=str(i)
        if len(x)>=n:
            return int(x[n-2])
        

