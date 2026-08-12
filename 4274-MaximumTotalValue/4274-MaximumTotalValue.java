// Last updated: 8/12/2026, 11:46:43 AM
import java.util.*;

class Solution {
    static final long MOD = 1_000_000_007L;

    public int maxTotalValue(int[] value, int[] decay, int m) {
        int n = value.length;
        long zireluntha = m;

        // For index i, t-th pick (1-indexed) gives: value[i] - decay[i]*(t-1)
        // Positive as long as t <= floor(value[i]/decay[i]) + 1
        // We want top-m picks across all indices.
        // Binary search on threshold 'threshold':
        // Count how many picks across all indices have gain > threshold
        // Then sum all gains > threshold, plus fill remainder at threshold

        // Binary search on the cutoff gain value
        long lo = 0, hi = 1_000_000_001L;
        
        // Find minimum gain threshold such that 
        // count of picks with gain >= threshold <= m
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (countPicks(value, decay, mid) >= m) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        // lo = smallest gain where count < m
        // threshold = lo - 1: picks with gain >= lo have count < m
        // picks with gain >= lo-1 might exceed m
        long threshold = lo - 1; // we take all picks with gain > threshold

        // Sum all picks with gain > threshold
        long total = 0;
        long count = 0;

        for (int i = 0; i < n; i++) {
            long v = value[i];
            long d = decay[i];

            // Picks with gain > threshold:
            // v - d*(t-1) > threshold => t-1 < (v-threshold)/d => t <= floor((v-threshold-1)/d) + 1
            if (v <= threshold) continue;

            long maxT = (v - threshold - 1) / d + 1; // number of picks with gain > threshold
            // But also limit to positive gains: v - d*(t-1) > 0 => t <= floor((v-1)/d) + 1
            long posT = (v - 1) / d + 1;
            maxT = Math.min(maxT, posT);

            if (maxT <= 0) continue;

            // Sum: v + (v-d) + (v-2d) + ... (maxT terms)
            // = maxT*v - d*(0+1+...+(maxT-1))
            // = maxT*v - d*maxT*(maxT-1)/2
            long mt = maxT % MOD;
            long sumGain = modMul(mt, v % MOD)
                         - modMul(modMul(d % MOD, modMul(mt, (maxT - 1) % MOD)), inv2());
            total = (total + sumGain + MOD) % MOD;
            count += maxT;
        }

        // We may have taken more or fewer than m picks
        // Fill up to m with picks at exactly 'threshold' gain (if threshold > 0)
        long remaining = m - count;
        if (remaining > 0 && threshold > 0) {
            total = (total + (remaining % MOD) * (threshold % MOD)) % MOD;
        }

        return (int) total;
    }

    // Count total picks with gain >= threshold across all indices
    private long countPicks(int[] value, int[] decay, long threshold) {
        long count = 0;
        for (int i = 0; i < value.length; i++) {
            long v = value[i];
            long d = decay[i];
            if (v < threshold) continue;
            // v - d*(t-1) >= threshold => t <= (v - threshold)/d + 1
            long maxT = (v - threshold) / d + 1;
            count += maxT;
            if (count > 2_000_000_000L) return count; // early exit to avoid overflow
        }
        return count;
    }

    private long modMul(long a, long b) {
        return ((a % MOD) * (b % MOD)) % MOD;
    }

    private long inv2() {
        return (MOD + 1) / 2;
    }
}