def ballsDistribution(colors, ballsPerColor, boxSize):

    currentBox = 0
    capacity = boxSize
    result = 0

    for i in range(colors):
        startBox = currentBox
        for j in range(ballsPerColor):
            capacity -= 1
            if capacity == 0:
                currentBox += 1
                capacity = boxSize
        if  startBox < currentBox and capacity<boxSize or startBox+1<currentBox:
            result += 1

    return result
