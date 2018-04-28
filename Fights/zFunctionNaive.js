function zFunctionNaive(s) {
  var result = [];
  for (var i = 0; i < s.length; i++) {
    result.push(0);
    for (var j = i; j < s.length; j++) {
      if (s[j] === s[result[i]]) {
        result[i]++;
      } else {
        break;
      }
    }
  }
  return result;
}
