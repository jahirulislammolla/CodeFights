def isLowerTriangularMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i][j]:
                return False
    return True
