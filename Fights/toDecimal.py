def toDecimal(k, n):

    result = 0
    power = 1
    for i in range(len(n) - 1, -1, -1):
        result += (ord(n[i]) - ord("0"))*power;
        power *= k
    return result
