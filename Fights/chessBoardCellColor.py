def chessBoardCellColor(cell1, cell2):

    def getX(pos):
        return ord(pos[0]) - ord('A')
    def getY(pos):
        return  ord(pos[0])-ord("A")

    sum1 = getX(cell1[0]) + getY(cell1[1])
    sum2 = getX(cell2[0]) + getY(cell2[1])
    if sum1 % 2 == sum2 % 2:
        return True
    return False
