def numberOfOperations(a, b):
    if a < b:
        a, b = b, a
    print(a,b)
    if a % b != 0:
        return 0
    return 1 + numberOfOperations(a // b, b)
