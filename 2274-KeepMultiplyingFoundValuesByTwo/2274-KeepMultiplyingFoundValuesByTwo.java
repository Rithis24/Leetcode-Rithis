// Last updated: 8/12/2026, 11:47:00 AM
class Solution {
    public int findFinalValue(int[] nums, int original) {
        HashSet<Integer> set = new HashSet<>();
        for (int n : nums) {
            set.add(n);
        }
        while (set.contains(original)) {
            original *= 2;
        }
        return original;
    }
}
