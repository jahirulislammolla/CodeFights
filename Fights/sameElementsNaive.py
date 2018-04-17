def sameElementsNaive(a, b):

    result = 0

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result += 1
    return result
