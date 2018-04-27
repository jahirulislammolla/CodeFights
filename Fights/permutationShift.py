def permutationShift(permutation):
    a=[permutation[i]-i for i in range(len(permutation))]
    return max(a)-min(a)
