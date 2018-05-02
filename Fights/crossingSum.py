def crossingSum(matrix, a, b):
    s=0
    for j in range(len(matrix[0])):
           s+=matrix[a][j]
    for j in range(len(matrix)):
           s+=matrix[j][b]
            
    return s-matrix[1]
