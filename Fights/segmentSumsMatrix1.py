def segmentSumsMatrix1(inputArray):

    answer = []
    for i in range(len(inputArray)):
        line = []
        for j in range(len(inputArray)):
            line.append(0)
        answer.append(line)

    for i in range(len(inputArray)):
        for j in range(i, -1, -1):
            for k in range(i, len(inputArray)):
                answer[j][k] += inputArray[i]
                answer[k][j] += inputArray[i]
        answer[i][i] -= inputArray[i]

    return answer
