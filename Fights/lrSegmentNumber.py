def lrSegmentNumber(l, r):
    result = 0
    while l <= r:
        result =  result*10+l 
        l += 1
    return result
