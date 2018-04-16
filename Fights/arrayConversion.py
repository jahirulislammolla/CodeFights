def arrayConversion(m):
    x=0
    while len(m)>1:
        y=[]
        for i in range(0,len(m),2):
            res=0
            if x%2==0:
                res+=m[i]+m[i+1]
            else:
                res+=m[i]*m[i+1]
            y.append(res)
        x+=1
        m=y
    return m[0]
        
        

