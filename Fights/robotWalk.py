def robotWalk(a):
    minX=0
    minY=-1
    maxX=9999999
    maxY=9999999
    x = 0
    y = 0
    for i in range(len(a)):
        k=i%4
        if k==0:
            y += a[i]
            if y >= maxY:
                return True
            maxY = y
        if k==1:
            x += a[i]
            if x >= maxX: 
                return True
            maxX = x
        if k==2:
            y -= a[i]
            if y <= minY: 
                return True
            minY = y

        if k==3:
            x -= a[i]
            if x <= minX:
                return True
            minX = x
            

    return False
    
