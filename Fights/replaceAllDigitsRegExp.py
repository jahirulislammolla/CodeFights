def replaceAllDigitsRegExp(input):
    s=''
    for i in input:
        if "0"<=i<="9":
            s+="#"
        else:
            s+=i
    return s

