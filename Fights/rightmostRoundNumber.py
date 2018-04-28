def rightmostRoundNumber(inputArray):
    for i in range(len(inputArray)-1,-1,-1):
        if inputArray[i]%10==0: return i
    return -1
