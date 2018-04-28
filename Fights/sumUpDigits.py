def sumUpDigits(d):
    s=0
    for i in d:
        if "0"<=i<="9":
            s+=int(i)
    return s
