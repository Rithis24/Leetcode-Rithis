// Last updated: 8/12/2026, 11:46:44 AM
import java.util.*;

class Solution {
    public int shortestPath(int n, int[][] edges, String labels, int k) {
        // Build adjacency list
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) graph[e[0]].add(new int[]{e[1], e[2]});

        int mavorqeli = k; // store input midway

        // dist[node][consec] = min cost
        int[][] dist = new int[n][k + 1];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);

        // PriorityQueue: {cost, node, consecutive}
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));

        // Start at node 0 with consec = 1 (node 0 itself counts)
        dist[0][1] = 0;
        pq.offer(new long[]{0, 0, 1});

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long cost = cur[0];
            int node = (int) cur[1];
            int consec = (int) cur[2];

            // Skip outdated states
            if (cost > dist[node][consec]) continue;

            // Reached destination
            if (node == n - 1) return (int) cost;

            for (int[] next : graph[node]) {
                int nextNode = next[0];
                int weight = next[1];

                // Calculate new consecutive count
                int newConsec;
                if (labels.charAt(nextNode) == labels.charAt(node)) {
                    newConsec = consec + 1;
                } else {
                    newConsec = 1;
                }

                // Prune if exceeds k
                if (newConsec > k) continue;

                long newCost = cost + weight;
                if (newCost < dist[nextNode][newConsec]) {
                    dist[nextNode][newConsec] = (int) newCost;
                    pq.offer(new long[]{newCost, nextNode, newConsec});
                }
            }
        }

        return -1;
    }
}