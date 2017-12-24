def reverseBits(n):
    res = 0
    for i in range(16):
        res =  (res*2 + n%2)
        n //= 2
    return res
