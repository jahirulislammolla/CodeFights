function candles(candlesNumber, makeNew) {
    return candlesNumber + Math.floor((candlesNumber - 1) / (makeNew - 1));
}
def candles(candlesNumber, makeNew):
    burned = 0
    leftovers = 0
    while candlesNumber > 0:
        burned += candlesNumber
        leftovers += candlesNumber
        candlesNumber = leftovers // makeNew
        leftovers %= makeNew
    return burned
