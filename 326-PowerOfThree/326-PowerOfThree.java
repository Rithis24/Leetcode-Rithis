// Last updated: 8/12/2026, 11:49:50 AM
class Solution {
    public boolean isPowerOfThree(int n) {
        if (n < 1) return false;

        while (n % 3 == 0) {
            n /= 3;
        }

        return n == 1;
    }
}