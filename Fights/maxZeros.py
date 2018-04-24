def maxZeros(n):
    answer = 0
    maxZeros = 0
    for k in range(2, n + 1):
        numZeros = 0
        value = n
        while value:
            if value % k == 0:
                numZeros += 1
            value //=  k
        if numZeros > maxZeros:
            maxZeros = numZeros
            answer = k
    return answer
