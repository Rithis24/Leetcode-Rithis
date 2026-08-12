// Last updated: 8/12/2026, 11:52:31 AM
class Solution {
    public boolean isPalindrome(int x) {

        if (x < 0) return false;

        int original = x;
        int rev = 0;

        while (x != 0) {
            int digit = x % 10;
            x = x / 10;
            rev = rev * 10 + digit;
        }

        return original == rev;
    }
}