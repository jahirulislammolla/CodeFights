def questionCorrectionBot(question):
    a=", ".join([i.strip() for i in question.strip().split(",")])
    x=""
    c=0
    for i in a:
        if (i==" " or i=="?") and c==0:
            x+=i
            c=1
        elif i not in "? ":
            x+=i
            c=0
        else:
            c=1
    if x[-1]!="?":
        x+="?"
    return x[0].upper()+x[1:]
