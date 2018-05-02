def inversePermutation(permutation):
    x=[0]*len(permutation)
    for i in range(len(permutation)):
        x[permutation[i]-1]=i+1
    return x
