function maxSubmatrixSum(matrix, n, m) {
    const rows = matrix.length, columns = matrix[0].length;
    let r = [];
    for(i = 0;i <= rows - n;i++) {
        for(k = 0;k <= columns - m;k++) {
            s = 0;
            for(x = 0;x < n;x++) {
                for(y = 0;y < m;y++) {
                    
                    s += matrix[i + x][k + y]
                }
            }
            r.push(s);
        }
    }
    return Math.max(...r)
}
