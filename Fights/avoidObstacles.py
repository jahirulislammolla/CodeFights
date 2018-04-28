def avoidObstacles(inputArray):
    i=2
    while any(j%i==0 for j in inputArray):
        i+=1
    return i
