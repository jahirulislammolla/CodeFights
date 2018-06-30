ef perfectCity(d, de):
    x=list(map(int,d))
    y=list(map(int,de))
    a=abs(x[0]-y[0])
    b=abs(x[1]-y[1])
    s=abs(d[0]-de[0])
    t=abs(d[1]-de[1])
    print(a,b)
    res=0
    if s<t:
        res=b+d[1]-x[1]+de[1]-y[1]
        print(res)
        m=math.ceil((d[0]+de[0])/2)
        n=math.floor((d[0]+de[0])/2)
        res+=min(abs(n-d[0])+abs(n-de[0]),abs(m-d[0])+abs(m-de[0]))
    else:
        res=a+d[0]-x[0]+de[0]-y[0]
        m=math.ceil((d[1]+de[1])/2)
        n=math.floor((d[1]+de[1])/2)
        res+=min(abs(m-d[1])+abs(m-de[1]),abs(n-d[1])+abs(n-de[1]))
    return res
    
