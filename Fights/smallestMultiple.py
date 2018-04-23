def smallestMultiple(left, right):
    x=left
    while True:
        k=0
        for i in range(left,right+1):
            if x%i==0:
                k+=1
        if k==right-left+1:
            return x
        x+=1
