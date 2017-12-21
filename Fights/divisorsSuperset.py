def divisorsSuperset(superset, n):

    def isInSequence(sequence, elem):
        for i in range(len(sequence)):
            if sequence[i]==elem:
                return True
        return False

    res = 0

    for i in range(1, n + 1):
        correct = True
        j = 2
        while j * j <= i:
            if i % j == 0:
                if not isInSequence(superset, j) or not isInSequence(superset, i / j):
                    correct = False
                    break
            j += 1
        if correct:
            res += 1

    return res
print (divisorsSuperset([2,3],13))
