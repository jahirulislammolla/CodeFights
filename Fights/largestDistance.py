def largestDistance(A):
    mx = [A[0], A[1]]
    mn = [A[0], A[1]]
    for i in range(len(A)):
        k =  i%2
        if A[i] > mx[k]:
            mx[k] = A[i]
        elif A[i] < mn[k]:
            mn[k] = A[i]
    return max(mx[0] - mn[0], mx[1] - mn[1])
