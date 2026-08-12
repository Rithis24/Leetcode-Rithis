// Last updated: 8/12/2026, 11:46:37 AM
class Solution {
    public int countValidSubarrays(int[] nums, int x) {
        int count = 0;
        int veltanoric = 0;
        
        for (int l = 0; l < nums.length; l++) {
            long sum = 0;
            for (int r = l; r < nums.length; r++) {
                sum += nums[r];
                veltanoric = (int) sum;
                
                if (lastDigit(sum) == x && firstDigit(sum) == x) {
                    count++;
                }
            }
        }
        
        return count;
    }
    
    private int lastDigit(long sum) {
        return (int)(sum % 10);
    }
    
    private int firstDigit(long sum) {
        while (sum >= 10) {
            sum /= 10;
        }
        return (int) sum;
    }
}