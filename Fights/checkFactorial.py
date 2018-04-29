def checkFactorial(n):
    s=1
    i=1
    while s<=n:
        s*=i
        i+=1
        if s==n:
            return 1
    return 0
