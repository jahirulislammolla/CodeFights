def mySqrt(n):

    left = 1
    right = n + 1
    while left + 1 < right:
        middle = (left + right) // 2
        if middle * middle <= n:
            left = middle
        else:
            right =  middle

    return left
