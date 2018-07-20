def brothersInTheBar(glasses):
    x=[]
    value=0
    count=1
    le=0
    reminder=glasses[0]
    for i in range(1,len(glasses)):
        if reminder==glasses[i]:
            count+=1
        else:
            l=count//3
            value+=l
            if count%3==0:
                if len(x)>0 and x[-1][0]==glasses[i]:
                    count=x[-1][1]+1
                    x.pop()
                else:
                    count=1
            else:
                x+=[[reminder,count%3]]
                count=1
            reminder=glasses[i]
    l=count//3
    value+=l
    return value
