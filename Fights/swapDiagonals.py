def swapDiagonals(matrix):
    size = len(matrix)
    for i in range(0,size/2):
        temp = matrix[i][i]
        matrix[i][i] = matrix[i][size-i-1]
        matrix[i][size-i-1] = temp
        temp = matrix[size-i-1][i]
        matrix[size-i-1][i] = matrix[size-i-1][size-i-1]
        matrix[size-i-1][size-i-1] = temp
    return matrix
