int bfsDistancesUnweightedGraph2(std::vector<std::vector<bool>> matrix, int vertex1, int vertex2) {

  bool visited[matrix.size()];
  std::fill_n(visited, matrix.size(), false);
  std::queue<int> q;
  std::vector<int> distance(matrix.size());

  visited[vertex1] = true;
  q.push(vertex1);
  while (q.size() > 0) {
    int currentVertex = q.front();
    q.pop();
    visited[currentVertex] = true;
    for (int nextVertex = 0; nextVertex < matrix.size(); ++nextVertex) {
      if (matrix[currentVertex][nextVertex] && !visited[nextVertex]) {
        visited[nextVertex] = true;
        distance[nextVertex] = distance[currentVertex] + 1;
        q.push(nextVertex);
      }
    }
  }

  return distance[vertex2];
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
