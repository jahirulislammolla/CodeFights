def stringsCrossover(inputArray, result):

    answer = 0

    for i in range(len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            correct = True
            for k in range(len(result)):
                if (result[k] != inputArray[i][k]
                  and result[k] != inputArray[j][k]):
                    correct=False
                    break
            if correct:
                answer += 1
    return answer
