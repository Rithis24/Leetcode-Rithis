# Last updated: 8/12/2026, 11:49:00 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first k elements to initialize the sliding window
        current_window_sum = sum(nums[:k])
        max_sum = current_window_sum

        # Slide the window across the rest of the array
        # The window starts at index 0 and ends at k-1.
        # For the next window, it starts at 1 and ends at k.
        # This means we iterate from index k up to len(nums) - 1.
        for i in range(k, len(nums)):
            # To slide the window, subtract the element that is leaving the window
            # (which is nums[i-k]) and add the new element entering the window (nums[i]).
            current_window_sum = current_window_sum - nums[i - k] + nums[i]
            # Update the maximum sum found so far
            max_sum = max(max_sum, current_window_sum)
        
        # The maximum average is the maximum sum divided by k
        return max_sum / k