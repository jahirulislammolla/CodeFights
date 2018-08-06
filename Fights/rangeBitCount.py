def rangeBitCount(a, b):

    ans = 0
    for i in range(a, b + 1):
        t = i
        while t != 0:
            ans += t & 1
            t >>= 1

    return ans
