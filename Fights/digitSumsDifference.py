def digitSumsDifference(n):

    result = 0
    while n != 0:
        digit = n // 10
        if digit % 2 == 1:
            result -= digit
        else:
            result += digit
        n //= 10

    return result
