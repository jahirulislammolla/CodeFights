def greatestCommonPrimeDivisor(a, b):

    gcd = -1
    divisor = 2
    while a > 1 and b > 1:
        if a % divisor == 0 and b % divisor == 0:
            gcd = divisor
        while a % divisor == 0:
            a /= divisor
        while b % divisor == 0:
            b /= divisor
        divisor += 1
    return gcd
