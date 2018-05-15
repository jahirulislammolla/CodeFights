def countWaysToChangeDigit(value):
    s=0
    while value>0:
        s+=(9-value%10)
        value//=10
    return s
