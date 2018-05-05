function countIncreasingSequences(n, k) {

  /*
   * array dp (short for dynamic programming)
   * is used for storing the interim values.
   */
  var dp = [];
  var sum = 0;

  for (var i = 0; i <= n; i++) {
    var line = [];
    for (var j = 0; j <= k; j++) {
      line.push(0);
    }
    dp.push(line);
  }
  dp[0][0] = 1;

  for (var i = 1; i <= n; i++) {
    for (var j = 1; j <= k; j++) {
      for (var q = 0; q < j; q++) {
        dp[i][j] += dp[i - 1][q];
      }
    }
  }
  for (var y = n, x=0; x<=k; x++)
    sum += dp[y][x];

  return sum;
}
