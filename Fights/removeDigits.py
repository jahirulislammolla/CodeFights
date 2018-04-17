def removeDigits(n, k):
    s=str(n)
    d=0
    f=999999999
    for i in range(0,len(s)-k+1):
        if int(s[i:i+k])>d:
            d=int(s[i:i+k])
        if int(s[i:i+k])<f:
            f=int(s[i:i+k])
    return [f,d]

