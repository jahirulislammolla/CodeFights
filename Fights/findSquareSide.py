def findSquareSide(x, y):
    return min((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2 for i in range(1, len(x)))
