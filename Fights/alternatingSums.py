def alternatingSums(a):
    s=0
    d=0
    for i in range(len(a)):
        if i%2==0:
            s+=a[i]
        else:
            d+=a[i]
    return [s,d]
