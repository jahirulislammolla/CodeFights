def trailingZeros(n):
    answer = 0
    while n % 2 == 0:
        n //= 2
        answer += 1
    return answer
