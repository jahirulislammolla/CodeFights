function prefixFunctionNaive(s) {

  var result = [];

  for (var i = 0; i < s.length; i++) {
    result.push(0);
    for (result[i] = i; result[i] >= 0; result[i]--) {
      var matches = true;
      for (var j = i - result[i] + 1; j <= i; j++) {
        if (s[j] !== s[j - i + result[i] - 1]) {
          matches = false;
          break;
        }
      }
      if (matches) {
        break;
      }
    }
  }

  return result;
}
