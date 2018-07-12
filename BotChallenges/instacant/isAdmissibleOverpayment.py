def isAdmissibleOverpayment(prices, notes, x):
    pp=0
    for i,j in zip(prices,notes):
        m=0.0
        k=""
        if "%" in j:
            m=float(j.split("%")[0])
            k=j.split("%")[1].strip().split(" ")[0].lower()
        if k=="higher":
            n=i/(1+.01*m)
            pp+=i-n
        if k=="lower":
            n=i/(1-.01*m)
            pp-=n-i
    pp=round(pp,5)
    return pp<=x
        
