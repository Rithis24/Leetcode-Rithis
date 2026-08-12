// Last updated: 8/12/2026, 11:46:51 AM
class Solution {
    public long finishTime(int n, int[][] edges, int[] baseTime) {
        // Build children adjacency list
        List<List<Integer>> children = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            children.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            children.get(edge[0]).add(edge[1]);
        }
        
        long[] finish = new long[n];
        
        // Iterative post-order traversal using explicit stack
        int[] stack = new int[n];
        boolean[] visited = new boolean[n];
        int top = 0;
        stack[top++] = 0;
        
        // order in which nodes get fully processed (post-order)
        int[] postOrder = new int[n];
        int postIdx = 0;
        int[] procStack = new int[n];
        int procTop = 0;
        procStack[procTop++] = 0;
        boolean[] pushed = new boolean[n];
        
        // Use a manual stack with state to do post-order without recursion
        Deque<int[]> st = new ArrayDeque<>(); // [node, childIndexToProcessNext]
        st.push(new int[]{0, 0});
        boolean[] onStack = new boolean[n];
        onStack[0] = true;
        
        while (!st.isEmpty()) {
            int[] frame = st.peek();
            int node = frame[0];
            List<Integer> kids = children.get(node);
            
            if (frame[1] < kids.size()) {
                int childIdx = frame[1];
                frame[1]++;
                int child = kids.get(childIdx);
                st.push(new int[]{child, 0});
            } else {
                // all children processed, compute finish time for this node
                st.pop();
                if (kids.isEmpty()) {
                    finish[node] = baseTime[node];
                } else {
                    long earliest = Long.MAX_VALUE;
                    long latest = Long.MIN_VALUE;
                    for (int child : kids) {
                        earliest = Math.min(earliest, finish[child]);
                        latest = Math.max(latest, finish[child]);
                    }
                    long ownDuration = (latest - earliest) + baseTime[node];
                    finish[node] = latest + ownDuration;
                }
            }
        }
        
        return finish[0];
    }
}