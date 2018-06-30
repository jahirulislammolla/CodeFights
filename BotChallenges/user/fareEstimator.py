def fareEstimator(t, d, cmi, cm):
    x=[]
    for i,j in zip(cmi,cm):
        p=t*i+d*j
        x.append(p)
    return x
