def factorSum(n):

    prevValue = 0
    currentValue = 0
    nextValue = n

    while nextValue != prevValue:
        divisor = 2
        currentValue = nextValue
        prevValue = nextValue
        nextValue = 0
        while divisor * divisor <= currentValue:
            if currentValue % divisor == 0:
                currentValue /= divisor
                nextValue += divisor
            else:
                divisor += 1
        nextValue += currentValue

    return nextValue
