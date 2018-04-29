function lazyFriends(houses, maxDist) {
    r = []
    for(i = 0;i < houses.length;i++) {
        c = 0;
        for(k = 0;k < houses.length;k++) {
            if(i === k) continue;
            if(Math.abs(houses[i] - houses[k]) <= maxDist) c++;
        }
        r.push(c)
    }
    return r
}
