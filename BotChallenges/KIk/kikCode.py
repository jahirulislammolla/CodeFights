def kikCode(userId):
    x='{0:060b}'.format(int(userId))[-52:][::-1]
    c=0
    mm=1
    result=[]
    for i in [3,4,8,10,12,15]:
        m=x[c:c+i]
        d=[]
        e={}
        l=360//i
        tt=0
        for j in range(1,i+1):
            if m[j-1]=="1":
                d+=[j]
            e[j]=tt
            tt+=l
        if len(d)==i:
            result.append([[mm,0],[mm,360]])
        elif len(d)>0:
            b=1
            if d[0]==1 and d[-1]==i:
                b+=i-1
                while b>0:
                    if b in d:
                        b-=1
                    else:
                        b+=1
                        break
            xx=[]
            for j in range(b,b+i+1):
                pp=j
                if j>i:
                    pp=j%i
                if pp in d:
                    xx+=[pp]
                else:
                    if len(xx)>0:
                        result.append([[mm,e[xx[0]]],[mm,e[xx[0]]+len(xx)*l]]) 
                    xx=[]
        c+=i
        mm+=1
    return result
