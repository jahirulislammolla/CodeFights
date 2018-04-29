def passwordCheckRegExp(s):
    if len(s)>=5:
        a,b,c=0,0,0
        for i in s:
            if "a"<=i<="z":
                a=1
            if "A"<=i<="Z":
                b=1
            if "0"<=i<="9":
                c=1
        return (a and b and c)
