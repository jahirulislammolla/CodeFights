def createAnagram(s, t):
    from collections import Counter
    
    c1 = Counter(s)
    c2 = Counter(t)
    ss = 0
    for k in set(s) | set(t):
        ss += abs(c1[k] - c2[k])
    return ss // 2
