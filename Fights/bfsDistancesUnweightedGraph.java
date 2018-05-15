int bfsDistancesUnweightedGraph2(boolean[][] matrix, int vertex1, int vertex2) {

  boolean[] visited = new boolean[matrix.length];
  LinkedList<Integer> queue = new LinkedList<>();
  int[] distance = new int[matrix.length];

  visited[vertex1] =  true ;
  queue.add(vertex1);
  while (queue.size() > 0) {
    int currentVertex = queue.pop();
    visited[currentVertex] = true;
    for (int nextVertex = 0; nextVertex < matrix.length; nextVertex++) {
      if (matrix[currentVertex][nextVertex] && !visited[nextVertex]) {
        visited[nextVertex] = true;
        distance[nextVertex] = distance[currentVertex] + 1;
        queue.add(nextVertex);
      }
    }
  }

  return distance[vertex2];
}

int[] bfsDistancesUnweightedGraph(boolean[][] matrix, int startVertex) {
     boolean[] visited = new boolean[matrix.length];
		  LinkedList<Integer> queue = new LinkedList<>();
		  int[] distance = new int[matrix.length];

		  visited[startVertex] = true;
		  queue.add(startVertex);
		  while (queue.size() != 0) {
		    int currentVertex = queue.pop();
		    visited[currentVertex] = true;
		    for (int nextVertex = 0; nextVertex < matrix.length; nextVertex++) {
		      if (matrix[currentVertex][nextVertex] && !visited[nextVertex]) {
		        visited[nextVertex] = true;
		        distance[nextVertex] = distance[currentVertex] + 1;
		        queue.add(nextVertex);
		      }
		    }
		  }

		  return distance;

}


    private static int[] bfsDistancesUnweightedGraph(boolean[][] matrix, int startVertex) {
        int[] distances = new int[matrix.length];
        Queue<Integer> queue = new LinkedList<>();
        int number_of_nodes = matrix[startVertex].length - 1;
        boolean[] visited = new boolean[number_of_nodes + 1];
        int i, element;
        visited[startVertex] = true;
        queue.add(startVertex);
        while (!queue.isEmpty()) {
            distances[startVertex]++;
            element = queue.remove();
            i = element;
            System.out.print(i + "\t");
            while (i <= number_of_nodes) {
                if (matrix[element][i] && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
                i++;
            }
        }
        return distances;
}
int largestFullBinaryTree(int[] parent) {

  class Graph {
    ArrayList<Integer>[] edges;
    int maxBinTree;

    Graph(int[] parent) {
      maxBinTree = 1;
      edges = new ArrayList[parent.length];
      for (int i = 0; i < edges.length; i++) {
        edges[i] = new ArrayList();
      }
      for (int i = 1; i < parent.length; i++) {
        edges[parent[i]].add(i);
      }
    }

    int dfs(int v) {
      int firstMax = -1;
      int secondMax = -1;
      for (int u : edges[v]) {
        int curMax = dfs(u);
        if (curMax > firstMax) {
          secondMax = firstMax;
          firstMax = curMax;
        } else if (curMax > secondMax) {
          secondMax = curMax;
        }
      }
      if (secondMax == -1) {
        return 1;
      }
      int result = 1 + firstMax + secondMax ;
      if (result > maxBinTree) {
        maxBinTree = result;
      }
      return result;
    }
  }

  Graph g = new Graph(parent);
  g.dfs(0);
  return g.maxBinTree;
}
