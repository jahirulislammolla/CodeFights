def areIsomorphic(a, b):
    if len(a)!=len(b):
        return False
    for i,j in zip(a,b):
        if len(i)!=len(j):
            return False
    for i,j in zip(b,a):
        if len(i)!=len(j):
            return False
    return True
    
