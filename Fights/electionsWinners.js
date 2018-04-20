def electionsWinners(votes, k):
    m = max(votes)
    
    if k == 0:
        if votes.count(m) > 1:
            return 0
        else:
            return 1
    return sum(v+k > m for v in votes)

#....................########........>>>>>>>>>>
function electionsWinners(votes, k) {
 var currentMaxIndex = 0,
        cntLeaders = 0,
        result = 0;
    for (var i = 0; i < votes.length; i++) {
        if (votes[i] === votes[currentMaxIndex]) {
            cntLeaders++;
        }
        if (votes[i] > votes[currentMaxIndex]) {
            currentMaxIndex = i;
            cntLeaders = 1;
        }
    }
    for (var i = 0; i < votes.length; i++) {
        if (votes[i] + k > votes[currentMaxIndex]) {
            result++;
        }
        if (votes[i] + k === votes[currentMaxIndex] && currentMaxIndex === i &&
            cntLeaders === 1) {
            result++;
        }
    }
    return result;
}
