def IsaacRule(steps, number):
    x=[number]
    y=[]
    while steps>0:
        for i in x:
            if i>3 and i%3==1 and (i//3)%2==1 and i//3>1:
                y+=[i//3]
            y+=[i*2]
        x=list(set(y))
        y=[]
        steps-=1
    return len(x)
