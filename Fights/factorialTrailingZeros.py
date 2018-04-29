def factorialTrailingZeros(n):
    result = 0
    for i in range(5,n + 1):
        number = i
        while number % 5 == 0:
            number /= 5
            result += 1
    return result
