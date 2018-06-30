def deliveryFee(intervals, fees, deliveries):
    k=0
    c=0
    d=[]
    x={}
    for i,j in deliveries:
        p=i+(j/100)
        if k+1<len(intervals) and intervals[k]<=p<intervals[k+1]:
            c+=1
        elif k+1==len(intervals)and intervals[k]<=p<=23.59:
            c+=1
        else:
            d.append(c)
            k+=1
            c=1
    d.append(c)
    m=[]
    try:
        for i in range(max(len(fees),len(d))):
            m.append(fees[i]/d[i])
    except:
        return 0
    return len(set(m))<=1
