def replaceMiddle(arr):
    l=len(arr)
    if l%2==0:
        t=l//2
        m=(arr[t-1]+arr[t])
        return arr[:t-1]+[m]+arr[t+1:]
    return arr
