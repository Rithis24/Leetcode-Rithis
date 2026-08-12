// Last updated: 8/12/2026, 11:47:13 AM
class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        
        // Create adjacency list
        ArrayList<Integer>[] graph = new ArrayList[n];
        
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        // Add edges (bidirectional)
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            graph[u].add(v);
            graph[v].add(u);
        }

        boolean[] visited = new boolean[n];

        return dfs(source, destination, graph, visited);
    }

    private boolean dfs(int node, int destination, ArrayList<Integer>[] graph, boolean[] visited) {
        
        if (node == destination) {
            return true;
        }

        visited[node] = true;

        for (int neighbour : graph[node]) {
            if (!visited[neighbour]) {
                if (dfs(neighbour, destination, graph, visited)) {
                    return true;
                }
            }
        }

        return false;
    }
}