def higherVersion(ver1, ver2):
    f = lambda v: tuple(map(int, v.split('.')))
    return f(ver1) > f(ver2)
