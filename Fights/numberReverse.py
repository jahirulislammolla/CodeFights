def numberReverse(inputNumber):

    reversed = 0
    while inputNumber >= 0:
        reversed = reversed * 10 + inputNumber % 10
        inputNumber //= 10
    return
