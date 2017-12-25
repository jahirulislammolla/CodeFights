def isMAC48Address(i):
    x=i.split("-")
    l=len(x)
    if l<6 or l>6:
        return 0
    for i in x:
        c=d=0
        if len(i)<2 or len(i)>2:
            return 0
        if ("A"<=i[0]<"G" or "0"<=i[0]<="9"):
            c=1
        if ("A"<=i[1]<"G" or "0"<=i[1]<="9"):
            d=1
        if not c or not d:
            return 0
    return 1
