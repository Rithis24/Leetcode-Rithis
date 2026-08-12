// Last updated: 8/12/2026, 11:46:35 AM
class Solution {
    public int minLights(int[] lights) {
        int n = lights.length;
        
        // Step 1: use difference array to mark coverage ranges in O(1) per bulb
        int[] diff = new int[n + 1];
        for (int i = 0; i < n; i++) {
            if (lights[i] > 0) {
                int v = lights[i];
                int left = Math.max(0, i - v);
                int right = Math.min(n - 1, i + v);
                diff[left]++;
                diff[right + 1]--;
            }
        }
        
        // Build covered array via prefix sum - O(n)
        boolean[] covered = new boolean[n];
        int running = 0;
        for (int i = 0; i < n; i++) {
            running += diff[i];
            covered[i] = running > 0;
        }
        
        // Step 2: greedily cover uncovered positions with new bulbs (radius 1 each)
        int count = 0;
        int i = 0;
        while (i < n) {
            if (covered[i]) {
                i++;
                continue;
            }
            int bulbPos = Math.min(i + 1, n - 1);
            int coverRight = Math.min(bulbPos + 1, n - 1);
            count++;
            i = coverRight + 1;
        }
        
        return count;
    }
}