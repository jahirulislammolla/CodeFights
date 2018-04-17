function candles(candlesNumber, makeNew) {
    return candlesNumber + Math.floor((candlesNumber - 1) / (makeNew - 1));
}
