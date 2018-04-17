def rightTriangle(sides):
    x=sorted(sides)
    return x[0]**2+x[1]**2==x[2]**2
