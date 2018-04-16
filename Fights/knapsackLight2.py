def knapsackLight2(w1, w2, m):
    if w1+w2<=m:
        return "both"
    if w1<=m and w2>m:
        return "first"
    if w2<=m and w1>m:
        return "second"
    if w1>m and w2>m:
        return "none"
    return "either"
