def isInformationConsistent(evidences):

    for j in range(len(evidences[0])):
        innocent = False
        guilty = False
        for i in range(len(evidences)):
            cur = evidences[i][j]
            if cur == -1:
                innocent = True
            elif cur == 1:
                guilty = True

        if innocent and guilty:
            return False

    return True
