def directionOfReading(numbers):
    numbers=numbers
    y=[]
    for i in range(len(numbers)):
        k=0
        for j in range(len(numbers)):
            k=k*10+numbers[j]%10
            numbers[j]//=10
        y.append(k)
    return y
    
