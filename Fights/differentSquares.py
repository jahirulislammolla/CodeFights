def differentSquares(matrix):
    s=set()
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            s.add(tuple(matrix[i][j:j+2]+matrix[i+1][j:j+2]))
    return len(s)

function differentSquares(matrix) {
    const hashes = new Set();
    
    for(let i = 0; i < matrix.length - 1; i++) {
        for(let j = 0; j < matrix[0].length - 1; j++) {
            const hash = matrix[i][j] * 1000 + matrix[i + 1][j] * 100 + matrix[i][j + 1] * 10 + matrix[i + 1][j + 1];
            hashes.add(hash);
        }
    }
    
    return hashes.size;
}
