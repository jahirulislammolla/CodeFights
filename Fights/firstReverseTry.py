def firstReverseTry(arr):
    if len(arr)==0:
        return []
    x=arr[0]
    y=arr[-1]
    arr[0]=y
    arr[-1]=x
    return arr
