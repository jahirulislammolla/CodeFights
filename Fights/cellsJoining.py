def cellsJoining(table, coords):
    table = [list(i) for i in table]

    cols = [i for i, v in enumerate(table[0]) if v == '+']
    rows = [i for i, v in enumerate(table) if v[0] == '+']

    (maxRow, minCol), (minRow, maxCol) = coords

    R = rows[minRow:maxRow + 2]
    C = cols[minCol:maxCol + 2]

    for row in R:
        if row in (0, rows[-1]):
            for col in C[1:-1]:
                table[row][col] = '-'
        elif row in R[1:-1]:
            for col in range(C[0] + 1, C[-1]):
                table[row][col] = ' '

    for col in C:
        if col in (0, cols[-1]):
            for row in R[1:-1]:
                table[row][col] = '|'
        elif col in C[1:-1]:
            for row in range(R[0] + 1, R[-1]):
                table[row][col] = ' '

    table = [''.join(i) for i in table]
    return table
