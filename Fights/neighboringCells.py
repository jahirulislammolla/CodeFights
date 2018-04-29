def neighboringCells(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > 0:
                matrix[i][j] += 1
            if j > 0:
                matrix[i][j] += 1
            if j < len(matrix[i])-1:
                matrix[i][j] += 1
            if i < len(matrix)-1:
                matrix[i][j] += 1
    return matrix
