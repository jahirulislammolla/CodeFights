def divisorsSubset(subset, n):
    k = 0
    for i in range(1, n + 1):
        flag = True
        for x in subset:
            if i % x != 0:
                flag = False
        if flag:
            k += 1
    return k
