def countLineColorings(points, colors):
    c=colors
    i=1
    while i<points:
        c*=colors-1
        i+=1
    return c
