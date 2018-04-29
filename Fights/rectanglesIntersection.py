def rectanglesIntersection(a, b, c, d):

    intersection = []

    for i in range(2):
        if a[i] > b[i]:
            t = a[i]
            a[i] = b[i]
            b[i] = t
        if c[i] > d[i]:
            t = c[i]
            c[i] = d[i]
            d[i] = t
        if b[i] < c[i] or d[i] < a[i]:
            return 0
        intersection += [min(b[i], d[i]) - max(a[i], c[i])]

    return (intersection[0] * intersection[1])
