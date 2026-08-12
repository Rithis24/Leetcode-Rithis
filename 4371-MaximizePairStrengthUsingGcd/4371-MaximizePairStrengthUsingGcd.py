# Last updated: 8/12/2026, 11:46:26 AM
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        m=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                g=math.gcd(nums[i],nums[j])
                s=(nums[i]*nums[j])//(g*g)
                if s>m:
                    m=s
        return m            