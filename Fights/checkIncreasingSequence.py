def checkIncreasingSequence(seq):
    x=seq[0]
    for i in range(1,len(seq)):
        if seq[i]<=x:
            return False
        x=seq[i]
    return 1

