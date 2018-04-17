function newNumeralSystem(number) {
    let left = 'A',
        right = number;
    let res = [];
    while (left <= right) {
        res.push(left + ' + ' + right);
        left = String.fromCharCode(left.charCodeAt() + 1);
        right = String.fromCharCode(right.charCodeAt() - 1);
    }
    return res;
}
