def isGeometricProgression(sequence):
    return all(sequence[i]*sequence[0]==sequence[1]*sequence[i-1] for i in range(1,len(sequence)))
