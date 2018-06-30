def computerNetwork(n, network):
    x={}
    p={}
    q={}
    for i in range(1,n+1):
        x[i]={}
        p[i]=99999999999
        q[i]=0
    for i,j,k in network:
        if i!=j:
            x[i][j]=k
            x[j][i]=k
    s=0
    y={}
    m=[1]
    while len(m)>0:
        pp=[]
        for i in m:
            for j in x[i]:
                s=str(min(i,j))+str(max(i,j))
                if p[j]>q[i]+x[i][j] and s not in y:
                    p[j]=x[i][j]+q[i]
                    q[j]=p[j]
                    pp.append(j)
                    y[s]=0
        m=pp
    if n==1:
        return 0
    return p[n]
