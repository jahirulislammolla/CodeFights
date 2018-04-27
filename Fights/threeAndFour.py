def threeAndFour(n):
    x=[]
    for i in range(n+1):
        if i%3==i%4==0:
            x.append(i)
    return x
