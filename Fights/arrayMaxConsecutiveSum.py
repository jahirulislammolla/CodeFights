def arrayMaxConsecutiveSum(inputArray, k):
    Max = sum(inputArray[:k])
    Current = Max
    for i in range(k, len(inputArray)):
        Current+=(inputArray[i]-inputArray[i-k])
        Max = max(Max, Current)
    return Max
