def isMonotonous(sequence):
   
    k=1
    c=1
    for i in range(len(sequence)-1):
        if sequence[i]<sequence[i+1]:
            continue
        else:
            k=0
    for i in range(len(sequence)-1):
        if sequence[i]>sequence[i+1]:
            continue
        else:
            c=0
    return c | k
