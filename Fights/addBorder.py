def addBorder(p):
    x=len(p[0])
    a=[]
    d="*"*(x+2)
    a.append(d)
    for i in p:
        a.append("*"+i+"*")
    a.append(d)
    return a
