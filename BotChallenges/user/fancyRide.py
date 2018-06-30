def fancyRide(l, fares):
    x=["UberX", "UberXL", "UberPlus", "UberBlack" , "UberSUV"]
    y={}
    for i in range(len(fares)):
        y[l*fares[i]]=i
    e=0
    for i in sorted(y):
        if i<=20:
            e=i
    return x[y[e]]
