# Last updated: 8/12/2026, 11:52:20 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k_ptr = 0  # This pointer will track the position for the next non-val element

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k_ptr] = nums[i]
                k_ptr += 1
        
        return k_ptr