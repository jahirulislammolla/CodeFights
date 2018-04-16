function largestFullBinaryTree(parent) {

  var edges;
  var maxBinTree;

  var initGraph = function(parent) {
    maxBinTree = 1;
    edges = [];
    for (var i = 0; i < parent.length; i++) {
      edges.push([]);
    }
    for (var i = 1; i < parent.length; i++) {
      edges[parent[i]].push(i);
    }
  };

  var dfs = function(v) {
    var firstMax = -1;
    var secondMax = -1;
    for (var i = 0; i < edges[v].length; i++) {
      var curMax = dfs(edges[v][i]);
      if (curMax > firstMax) {
        secondMax = firstMax;
        firstMax = curMax;
      } else if (curMax > secondMax) {
        secondMax = curMax;
      }
    }
    if (secondMax === -1) {
      return 1;
    }
    var result = 1 + firstMax + secondMax;
    
    maxBinTree = Math.max(maxBinTree, result);
    
    return result;
  };

  initGraph(parent);
  dfs(0);
  return maxBinTree;
}
