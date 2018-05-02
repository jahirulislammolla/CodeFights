def pairOfShoes(shoes):
    leftShoes = []
    rightShoes = []
    for i in range(len(shoes)):
        if shoes[i][0] == 0:
            leftShoes.append(shoes[i][1])
        else:
            rightShoes.append(shoes[i][1])
    leftShoes.sort()
    rightShoes.sort()
    if len(leftShoes) != len(rightShoes):
        return False
    for i in range(len(leftShoes)):
        if leftShoes[i] != rightShoes[i]:
            return False
    return True
