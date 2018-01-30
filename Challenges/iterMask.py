from itertools import combinations
def iterMask(t):
    n=list("{:0b}".format(t))
    x=[]
    for i,j in enumerate(n):
        if j=="1":
            x+=[i]
    m=[t,0]
    for i in range(1,len(x)):
        for j in combinations(x,i):
            y=[]
            y+=n
            for k in j:
                y[k]="0"
            m+=[int("".join(y),2)]
    return sorted(m,reverse=True)
