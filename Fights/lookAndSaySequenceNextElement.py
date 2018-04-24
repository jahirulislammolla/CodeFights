def lookAndSaySequenceNextElement(inputString):

    consecutiveEqual = 1
    result = []
    inputString += '#'
    for i in range(1, len(inputString)):
        if inputString[i] != inputString[i - 1]:
            result.append(str(consecutiveEqual))
            result.append(inputString[i-1])
            consecutiveEqual = 1
        else:
            consecutiveEqual += 1

    return ''.join(result)
