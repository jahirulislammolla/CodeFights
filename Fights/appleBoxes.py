def appleBoxes(k):
    x = 0
    y = 0
    for i in range(1, k + 1):
        if i % 2 == 0:
            y+=i*i
        if i % 2 != 0:
            x+=i*i
    return y-x
