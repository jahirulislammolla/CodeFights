function chessKnightMoves(cell) {
    x = cell.charCodeAt(0)%97;
    y = cell.charCodeAt(1) - '0'.charCodeAt(0) - 1;
    c = 0;
    for ( dx = -2; dx <= 2; dx++)
        for (dy = -2; dy <= 2; dy++) {
            if (Math.abs(dx * dy) == 2)
                if (isValid(x + dx, y + dy))
                    c++;
        }
    return c;
}
function isValid(x, y) {
    return x >= 0 && x <= 7 && y >= 0 && y <= 7;
}
