// Last updated: 8/12/2026, 11:47:10 AM
class Solution {
    public int arraySign(int[] nums) {
        int negatives = 0;

        for (int num : nums) {
            if (num == 0) {
                return 0;
            }

            if (num < 0) {
                negatives++;
            }
        }

        return (negatives % 2 == 0) ? 1 : -1;
    }
}