def knapsackLight(v1, w1, v2, w2, m):
    if w1+w2<=m:
        return v1+v2
    if w1<=m and w2>m:
        return v1
    if w2<=m and w1>m:
        return v2
    if w1>m and w2>m:
        return 0
    return max(v1,v2)
