def arrayKthGreatestQuick(inputArray, k):

    pos = random.randint(0, len(inputArray) - 1)
    left = []
    right = []

    if len(inputArray) == 1:
        return inputArray[0]

    for i in range(len(inputArray)):
        if inputArray[i] <= inputArray[pos]:
            left.append(inputArray[i])
        else:
            right.append(inputArray[i])

    if len(right) >= k:
        return arrayKthGreatestQuick(right, k)
    return arrayKthGreatestQuick(left, k - len(right))
