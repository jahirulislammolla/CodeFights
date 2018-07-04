def composeRanges(nums):
    x=[]
    if len(nums)==0:
        return []
    p=str(nums[0])
    c=0
    for i in range(1,len(nums)):
        if nums[i-1]+1==nums[i]:
            c+=1
        else:
            if c>0:
                x.append(p+"->"+str(nums[i-1]))
            if c==0:
                x.append(str(nums[i-1]))
            p=str(nums[i])
            c=0
    if c>0:
        x.append(p+"->"+str(nums[-1]))
    if c==0:
        x.append(str(nums[-1]))
    return x
