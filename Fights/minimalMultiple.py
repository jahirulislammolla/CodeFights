def minimalMultiple(divisor, lowerBound):

    if lowerBound % divisor == 0:
        return lowerBound
    return (lowerBound // divisor + 1) * divisor
