def maximalAllowableSubarrays(inputArray, maxSum):

    right = [0] * len(inputArray)
    j = -1
    curSum = 0
    for i in range(len(inputArray)):
        if i > 0:
            curSum -= inputArray[i - 1]
        while j + 1 < len(inputArray) and curSum + inputArray[j + 1] <= maxSum:
            j += 1
            curSum += inputArray[j]
        right[i] = j

    return right
