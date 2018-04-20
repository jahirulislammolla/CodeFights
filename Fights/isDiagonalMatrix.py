def isDiagonalMatrix(m):
    l=len(m)
    for i in range(l):
        for  j in range(l):
            if i!=j and m[i][j]!=0:
                return 0
    return 1
