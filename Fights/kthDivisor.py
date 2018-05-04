def kthDivisor(n, k):
    divisors = []
    i = 1
    while i * i < n:
        if n % i == 0:
            divisors.append(i)
        i += 1
    if i * i > n:
        i -= 1
    while i > 0:
        if n % i == 0:
            divisors.append(n//i)
        i -= 1
    if len(divisors) < k:
        return -1
    return divisors[k - 1]
