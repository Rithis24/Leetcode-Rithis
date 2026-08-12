// Last updated: 8/12/2026, 11:50:13 AM
class Solution {
    public int rob(int[] nums) {
        int n=nums.length;
        if(n==1){
            return nums[0];
        }
        int[] ar=new int[n];
        ar[0]=nums[0];
        ar[1]=Math.max(nums[0],nums[1]);
        for(int i=2;i<n;i++){
            ar[i]=Math.max(ar[i-1],nums[i]+ar[i-2]);
        }
        return ar[n-1];
    }
}