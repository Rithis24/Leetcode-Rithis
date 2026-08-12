// Last updated: 8/12/2026, 11:51:19 AM
class Solution {
    public int singleNumber(int[] nums) {
    int result = 0;
    for (int num : nums) {
        result ^= num;
    }
    return result;
}
}