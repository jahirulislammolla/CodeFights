def domainType(domains):
    x=[]
    a=["com","org","net","info"]
    b=["commercial","organization","network","information"]
    for i in domains:
        x+=[b[a.index(i.split(".")[-1])]]
    return x
        
