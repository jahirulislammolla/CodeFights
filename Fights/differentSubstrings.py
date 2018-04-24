def differentSubstrings(s):
    x=[]
    for i in range(1,len(s)+1):
        for j in range(len(s)):
            x.append(s[j:j+i])
    return len(set(x))
