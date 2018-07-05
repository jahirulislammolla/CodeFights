def ratingThreshold(threshold, ratings):
    x=[]
    c=0
    for i in ratings:
        s=sum(i)/len(i)
        if s<threshold:
            x+=[c]
        c+=1
    return x
        
