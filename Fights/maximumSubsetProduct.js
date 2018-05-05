function maximumSubsetProduct(a) {
    let p = a.reduce((t, v) => t *= v, 1);
    if(p > 0) return 1;
    if(a.length === 1) return 1
    return Math.max(...a.filter(v => v < 0))
}
