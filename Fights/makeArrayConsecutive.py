def makeArrayConsecutive(s):
    x=[]
    for i in range(min(s),max(s)):
        if i not in s:
            x.append(i)
    return x
