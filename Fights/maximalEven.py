def maximalEven(inputArray):

    answer = 0
    for i in range(len(inputArray)):
        if  inputArray[i]>answer and inputArray[i]%2==0:
            answer = inputArray[i]
    return answer
