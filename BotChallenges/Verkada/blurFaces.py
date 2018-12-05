def blurFaces(img):
    x=[[0 for i in range(len(img[0]))] for j in range(len(img))]
    print(x)
    l=len(img)
    l1=len(img[0])
    for i in range(l):
        for j in range(l1):
            c=0
            e=-1
            for k in range(-1,2):
                for t in range(-1,2):
                    if 0<=k+i<l and 0<=t+j<l1:
                        # print(k+i,t+j)
                        c+=img[k+i][t+j]
                        e+=1
            x[i][j]=(c-img[i][j])/e
    return x
