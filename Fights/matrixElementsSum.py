def matrixElementsSum(matrix):
    s=0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j]!=0:
                s+=matrix[i][j]
            else:
                break
    return s
