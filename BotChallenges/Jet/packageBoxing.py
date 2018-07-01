def packageBoxing(pkg, boxes):
    x,y,z=sorted(pkg)
    d=-1
    f=9999999999
    c=0
    for a in boxes:
        i,j,k=sorted(a)
        if x<=i and y<=j and z<=k:
            if i*j*k<f:
                f=i*k*j
                d=c
        c+=1
    return d
