def checkSameElementExistence(arr1, arr2):
    x={}
    for j in arr2:
        x[j]=0
    for i in arr1:
        try:
           d=x[i]
           return 1
        except:
            continue
    return 0
            
