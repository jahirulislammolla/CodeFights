def fractionReducing(fraction):

    def gcd(a, b):
        if a > b:
            return gcd(b%a,a)
        if a == 0:
            return b
        return gcd(b % a, a)

    commonDivisor = gcd(fraction[0], fraction[1])
    fraction[0] /= commonDivisor
    fraction[1] /= commonDivisor

    return fraction
