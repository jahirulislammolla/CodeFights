def houseNumbersSum(inputArray):
    s=0
    for i in inputArray:
        if i==0:
            break
        s+=i
    return s
