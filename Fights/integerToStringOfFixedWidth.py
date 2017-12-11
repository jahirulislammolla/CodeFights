def integerToStringOfFixedWidth(number, width):
    s=str(number)
    l=len(s)
    if l<width:
        s="0"*(width-l)+s
    if l>width:
        s=s[l-width:]
    return s
