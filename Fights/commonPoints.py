def commonPoints(l1, r1, l2, r2):
    result = min(r1, r2) - max(l1, l2) - 1
    if result < 0:
        result = 0
    return result
