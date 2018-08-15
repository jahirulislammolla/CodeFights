def treeClimbing(branches, friends):
    c=0
    m=0
    su=0
    for i,j in friends:
        p=0
        q=0
        t=0
        f=0
        for k,l in branches:
            if c==0:
                if t<len(branches)-1:
                    m=max(m,abs(branches[t][0]-branches[t+1][0]))
                t+=1
                if k<=p+i:
                    if l>=j:
                        p=k
                else:
                    f=1
                    
            else:
                if k<=p+i and m<=i:
                    if l>=j:
                        p=k
                else:
                    f=1
                    break
        if f==0 and p==branches[-1][0]:
            su+=1
        c=1
    return su
