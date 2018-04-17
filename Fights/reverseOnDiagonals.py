def reverseOnDiagonals(matrix):
    x=[]
    for i in range(len(matrix)):
        x.append(matrix[i][i])
    y=[]
    l=len(matrix)-1
    for i in range(len(matrix)):
        y.append(matrix[l][i])
        l-=1
    l=-1
    x=x[::-1]
    y=y[::-1]
    for i in range(len(matrix)):
        matrix[i][i]=x[i]
        matrix[l][i]=y[i]
        l-=1
    return matrix
