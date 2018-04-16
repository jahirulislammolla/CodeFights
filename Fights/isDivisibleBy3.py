
def isDivisibleBy3(inputString):
    x=inputString.split("*")
    y=[]
    for i in range(10):
        m=str(i).join(x)
        if int(m)%3==0:
            y.append(m)
    return y
