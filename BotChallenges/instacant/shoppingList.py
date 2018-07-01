def shoppingList(items):
    x=[]
    c=""
    k=0
    for i in items:
        if "0"<=i<="9":
            c+=i
        elif i=="." and k<1:
            c+=i
            k+=1
        else:
            k=0
            if c!="":
                x.append(c)
            c=""
    if c!="":
        x.append(c)
    c=0
    for i in x:
        try:
            c+=float(i)
        except:
            continue
    return c
