def oddNumbersBeforeZero(sequence):

    result = 0
    for i in range(1, len(sequence)):
        if sequence[i] == 0:
            break
        if sequence[i] % 2 == 1:
            result += 1
    return result
