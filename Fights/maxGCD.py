def maxGCD(sequence):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    bestRes = 0

    for i in range(len(sequence)):
        result = sequence[0]
        if i == 0:
            result = sequence[1]
        for j in range(len(sequence)):
            if i == j:
                continue
            result = gcd(result, sequence[j])
        if result > bestRes:
            bestRes = result

    return bestRes
