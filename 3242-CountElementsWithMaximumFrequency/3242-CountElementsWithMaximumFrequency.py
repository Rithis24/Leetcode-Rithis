# Last updated: 8/12/2026, 11:46:55 AM
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)
        max_freq = max(freq.values())

        ans = 0
        for count in freq.values():
            if count == max_freq:
                ans += count

        return ans