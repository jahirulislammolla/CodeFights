def stolenLunch(note):
    x="0123456789"
    y="abcdefghij"
    d=""
    for i in note:
        if i in x:
            d+=y[x.index(i)]
        elif i in y:
            d+=x[y.index(i)]
        else:
            d+=i
    return d
