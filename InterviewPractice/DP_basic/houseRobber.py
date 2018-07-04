def houseRobber(nums):
    if len(nums)==0:
        return 0
    if len(nums)<3:
        return max(nums)
    x={}
    for i in range(len(nums)):
        x[i]=0
    def check(s,l):
        x[l]=s
        if l+3<len(nums) and s+nums[l+3]>x[l+3]:
            check(s+nums[l+3],l+3)
        if l+2<len(nums) and s+nums[l+2]>x[l+2]:
            check(s+nums[l+2],l+2)
        return 0
    check(nums[0],0)
    check(nums[1],1)
    return max(x.values())
