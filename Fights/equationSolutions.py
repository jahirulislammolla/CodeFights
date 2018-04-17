def equationSolutions(l, r):
    c=0
    for i in range(l,r+1):
        a=i**3
        for j in range(l,r+1):
            if a==j**2:
                c+=1
                
    return c
