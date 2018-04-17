def numberOfTriangles(sticks):
    res = 0
    for i in range(len(sticks)):
        k = i + 2
        for j in range(i + 1, len(sticks)):
            while k < len(sticks) or sticks[k] < sticks[i] + sticks[j]:
                k += 1
            res += k - j - 1
    return res
