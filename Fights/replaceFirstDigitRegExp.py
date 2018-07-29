def replaceFirstDigitRegExp(input):
    s=""
    k=0
    for i in input:
        if i in "0123456789" and k==0:
            s+="#"
            k=1
        else:
            s+=i
    return s

def replaceFirstDigitRegExp(inputString):
    return re.sub('[0-9]', '#', inputString,1)
