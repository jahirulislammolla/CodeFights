def differentValues(a, d):

    best = -1
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            diff = abs(a[j] - a[i])
            if  best<diff and diff<=d :
                best = diff

    return best
