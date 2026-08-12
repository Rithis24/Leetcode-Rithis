// Last updated: 8/12/2026, 11:52:02 AM
class Solution {
    public double myPow(double x, int n) {
        long exp = n;

        if (exp < 0) {
            x = 1 / x;
            exp = -exp;
        }

        double result = 1;

        while (exp > 0) {
            if ((exp & 1) == 1) {
                result *= x;
            }
            x *= x;
            exp >>= 1;
        }

        return result;
    }
}
