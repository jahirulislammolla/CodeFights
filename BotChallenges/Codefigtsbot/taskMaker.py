def taskMaker(s, c):
    x=[]
    for i in s:
        m=i.split("//")
        if len(m)==3 and str(c) in m[1]:
            del x[-1]
            x+=[m[0]+m[2]]
        if len(m)==1:
            x+=[i]
    return x
            
