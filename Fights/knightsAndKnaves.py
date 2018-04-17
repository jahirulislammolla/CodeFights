def knightsAndKnaves(answers):

    n = len(answers)
    isKnight = [False] * n
    isKnight[0] = True
    for i in range(1, n):
        isKnight[i] = (answers[0] >> i & 1)
    for i in range(n):
        for j in range(n):
            if ((isKnight[i] == isKnight[j]) ^
                    (answers[i] >> j & 1)):
                return False

    return True
