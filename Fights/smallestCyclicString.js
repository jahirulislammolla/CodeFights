function smallestCyclicString(inputString) {

  var P = 997,
      M = 28001,
      hash,
      powP;

  var buildHash = function(s) {
    hash = [0];
    powP = [1];
    for (var i = 1; i <= s.length; i++) {
      hash.push((hash[i - 1] * P + s.charCodeAt(i - 1)) % M);
      powP.push((powP[i - 1] * P) % M);
    }
  };

  // Hash of substring with indices [l, r)
  var substrHash = function(l, r) {
    return (hash[r] - (hash[l] * powP[r - l] % M) + M) % M;
  };

  var n = inputString.length;
  inputString += inputString;
  buildHash(inputString);
  var bestShift = 0;
  for (var i = 1; i < n; i++) {
    var l = 0,
        r = n;
    while (r - l > 1) {
      var m = Math.floor((l + r) / 2);
      if (substrHash(bestShift, bestShift + m) ===
          substrHash(i, i + m)) {
        l = m;
      } else {
        r = m;
      }
    }

    var commonPrefixLen = l;
    if (inputString[bestShift + commonPrefixLen] >
        inputString[i + commonPrefixLen]) {
      bestShift = i;
    }
  }

  return inputString.substring(bestShift, bestShift + n);
}
