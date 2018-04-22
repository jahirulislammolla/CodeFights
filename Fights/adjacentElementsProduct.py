def adjacentElementsProduct(inputArray):

    best = inputArray[0] * inputArray[1]
    cur = best
    for i in range(1, len(inputArray) - 1):
        cur = inputArray[i] * inputArray[i+1]
        if best < cur:
            best = cur

    return best
