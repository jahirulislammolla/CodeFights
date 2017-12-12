def bitsToFloat(bits):
    intp = int(bits >> 16)
    frap = float(bits & 0xFFFF)
    while frap >= 1.:
        frap /= 10.
    return intp + frap
