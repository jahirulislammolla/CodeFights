def countTriangles(X,Y):
    l=len(X)
    c=0
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                x1 = X[i] - X[j]
                y1 = Y[i] - Y[j]
                x2 = X[i] - X[k]
                y2 = Y[i] - Y[k]
                if x1*y2 != x2*y1:
                    c+=1
    return c
                

