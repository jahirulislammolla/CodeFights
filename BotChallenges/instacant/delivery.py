def delivery(order, shoppers):
    x,y,z=order
    p=[]
    for i,j,k in shoppers:
        m=(i+x)/j+k
        if y<=m<=y+z:
            p.append(True)
        else:
            p.append(False)
    return p
