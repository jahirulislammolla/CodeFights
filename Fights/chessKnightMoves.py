def chessKnightMoves(cell):
    x=ord(cell[0])-97
    y=ord(cell[1])-49
    c=0
    for i in range(-2,3):
        for j in range(-2,3):
            if abs(i*j)==2:
                if (check(x+i,y+j)):
                    c+=1
    return c
def check(x,y):
    return x >= 0 and x <= 7 and y >= 0 and y <= 7
