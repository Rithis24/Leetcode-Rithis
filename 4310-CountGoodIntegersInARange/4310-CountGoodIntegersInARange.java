// Last updated: 8/12/2026, 11:46:39 AM
import java.util.Arrays;

class Solution {
    private String numStr;
    private int K;
    private long[][][] memo; // [pos][prevDigit+1][started]
    
    public long goodIntegers(long l, long r, int k) {
        this.K = k;
        long countR = countUpTo(r);
        long countL = (l > 0) ? countUpTo(l - 1) : 0;
        return countR - countL;
    }
    
    private long countUpTo(long x) {
        if (x < 0) return 0;
        numStr = Long.toString(x);
        int n = numStr.length();
        // memo[pos][prevDigit + 1][started] -- prevDigit ranges -1..9, so +1 offset -> 0..10
        memo = new long[n][11][2];
        for (long[][] a : memo) {
            for (long[] b : a) {
                Arrays.fill(b, -1);
            }
        }
        return dfs(0, -1, true, false);
    }
    
    // pos: current digit index
    // prevDigit: last placed digit (-1 if none placed yet, i.e., still in leading zeros)
    // tight: whether prefix so far equals x's prefix
    // started: whether a digit (after leading zeros) has been placed
    private long dfs(int pos, int prevDigit, boolean tight, boolean started) {
        int n = numStr.length();
        if (pos == n) {
            return started ? 1 : 0;
        }
        
        if (!tight && memo[pos][prevDigit + 1][started ? 1 : 0] != -1) {
            return memo[pos][prevDigit + 1][started ? 1 : 0];
        }
        
        int maxDigit = tight ? (numStr.charAt(pos) - '0') : 9;
        long total = 0;
        
        for (int d = 0; d <= maxDigit; d++) {
            boolean newTight = tight && (d == maxDigit);
            
            if (!started && d == 0) {
                // still in leading zeros, skip adjacency check
                total += dfs(pos + 1, -1, newTight, false);
            } else {
                if (started && Math.abs(d - prevDigit) > K) {
                    continue; // violates adjacency constraint
                }
                total += dfs(pos + 1, d, newTight, true);
            }
        }
        
        if (!tight) {
            memo[pos][prevDigit + 1][started ? 1 : 0] = total;
        }
        
        return total;
    }
}