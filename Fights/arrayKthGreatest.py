def arrayKthGreatest(inputArray, k):

    for i in range(k):
        indexOfMaximum = i
        tmp = inputArray[i]

        for j in range(i + 1, len(inputArray)):
            if inputArray[j] > inputArray[indexOfMaximum]:
                indexOfMaximum=j

        inputArray[i] = inputArray[indexOfMaximum]
        inputArray[indexOfMaximum] = tmp

    return inputArray[k - 1]
