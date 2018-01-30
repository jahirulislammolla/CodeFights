def areaOfIntersection(s1, s2):
    xmi = max(s1[1]+s1[2]-(s1[0]-1),s2[1]+s2[2]-(s2[0]-1))
    xma = min(s1[1]+s1[2]+(s1[0]-1),s2[1]+s2[2]+(s2[0]-1))
    ymi= max(s1[1]-s1[2]-(s1[0]-1),s2[1]-s2[2]-(s2[0]-1))
    yma = min(s1[1]-s1[2]+(s1[0]-1),s2[1]-s2[2]+(s2[0]-1))
    if(xmi > xma or ymi> yma):
        return 0
    else:
        eX = (xma-xmi +2) // 2 if (0==xmi%2) else (xma-xmi+1) // 2
        oX = (xma-xmi-eX+1)
        eY = (yma-ymi+2) // 2 if (0==ymi%2) else (yma-ymi+1) // 2
        oY = (yma-ymi-eY+1)
        return eX*eY+oX*oY
