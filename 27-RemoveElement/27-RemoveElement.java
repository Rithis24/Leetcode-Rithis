// Last updated: 8/12/2026, 11:52:25 AM
class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0; // index for placing elements not equal to val

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }
}
