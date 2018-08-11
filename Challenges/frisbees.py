def frisbees(friends, numberOfPasses, startingPlayer):
    x={}
    y={}
    z={}
    a={}
    c=0
    for i,j,k in friends:
        if i not in x:
            x[i]=[]
        a[c]=[[],[]]
        x[i]+=[[j,c]]
        y[c]=0
        c+=1
    c=0
    z=sorted(x)
    for i,j,k in friends:
        for p in z:
            if i-k<=p<=i+k:
                for m,o in sorted(x[p]):
                    if j-k<=m<=j+k and o!=c:
                        d=((i-p)**2+(j-m)**2)
                        if d<=k*k:
                            a[c][0]+=[o]
                            a[c][1]+=[d]
                    elif m>j+k:
                        break
            elif p>i+k:
                break
        c+=1
    i=0
    index=startingPlayer
    while i<numberOfPasses:
        val1=9999999
        ma=0
        y[startingPlayer]+=1
        for j in range(len(a[startingPlayer][0])):
            p=y[a[startingPlayer][0][j]]
            if p==val1:
                if ma==a[startingPlayer][1][j]:
                    index=min(index,a[startingPlayer][0][j])
                if ma<a[startingPlayer][1][j]:
                    ma=a[startingPlayer][1][j]
                    index=a[startingPlayer][0][j]
            if p<val1:
                val1=p
                index=a[startingPlayer][0][j]
                ma=a[startingPlayer][1][j]
        startingPlayer=index
        i+=1
    return startingPlayer
            
                    
