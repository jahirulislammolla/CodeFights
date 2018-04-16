def differentSymbolsNaive(s):
    x=[]
    for i in s:
        if "a"<=i<="z":
            if i not in x:
                x.append(i)
    return len(x)
            

