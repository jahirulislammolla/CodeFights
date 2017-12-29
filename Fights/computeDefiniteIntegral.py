def computeDefiniteIntegral(l, r, p):
    x=0
    for i,j in enumerate(p):
        if j !=0:
            x+=j*(((r**(i+1))/(i+1))-((l**(i+1))/(i+1)))
    return x
