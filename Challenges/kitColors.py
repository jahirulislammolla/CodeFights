def kitColors(first, second):
    x={}
    for i in first:
        for j in second:
            kk=0
            for k in range(1,len(i),2):
                s=int(i[k:k+2],16)
                p=int(j[k:k+2],16)
                kk+=abs(s-p)
            if kk not in x:
                x[kk]=[]
            x[kk]+=[[i,j]]
    return x[max(x)]

