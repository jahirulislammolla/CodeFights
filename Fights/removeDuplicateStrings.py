def removeDuplicateStrings(inputArray):
    result = []
    for i in range(len(inputArray)):
        if i + 1 != len(inputArray) and inputArray[i] == inputArray[i + 1]:
            continue
        result.append(inputArray[i])
    return result
