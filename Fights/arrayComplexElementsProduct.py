
def arrayComplexElementsProduct(real, imag):
    curx = real[0]
    cury = imag[0]

    for x, y in zip(real[1:], imag[1:]):
        newx = curx * x - cury * y
        newy = curx * y + cury * x
        curx, cury = newx, newy
    return [curx, cury]
