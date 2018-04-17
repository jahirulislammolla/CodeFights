def evenDigitsOnly(n):
    while n>0:
        if n%2!=0:
            return 0
        n//=10
    return 1
