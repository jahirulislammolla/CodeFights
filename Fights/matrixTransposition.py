def matrixTransposition(matrix):
    x=[]
    for i in zip(*matrix):
        m=list(i)
        x.append(m)
    return x
