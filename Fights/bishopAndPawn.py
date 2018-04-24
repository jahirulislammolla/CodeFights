def bishopAndPawn(bishop, pawn):
    x=abs(ord(bishop[0])-ord(pawn[0]))
    y=abs(int(bishop[1])-int(pawn[1]))
    if x==y:
          return True
    return False
