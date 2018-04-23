function increaseNumberRoundness(n) {
    n = n.toString();
    while(n.endsWith('0')) {
        n = n.substr(0, n.length - 1);
    }
    if(n.includes('0')) return true;
    return false
}
