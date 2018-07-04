def isCryptSolution(crypt, solution):
    a,b={},[]
    for x,y in solution:
        a[x]=y
    for i in crypt:
        c=''
        for j in i:
            c+=a[j]
        if c[0]=="0" and len(c)>1:
            return 0
        b+=[c]
    return int(b[0])+int(b[1])==int(b[2])
