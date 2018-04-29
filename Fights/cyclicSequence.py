def cyclicSequence(sequence):
    d=0
    if len(sequence)==1:
        return 1
    if len(sequence)>len(set(sequence)):
        return 0
    for i in range(len(sequence)-1):
        if sequence[i]>sequence[i+1]:
            d=i+1
            break
    if d!=0:
        return sorted(sequence)==sequence[i+1:]+sequence[:i+1]
    if d==0:
        return 1
    return 0        
