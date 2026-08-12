# Last updated: 8/12/2026, 11:49:28 AM
class Solution:
    def findMaxLength(self, nums):
        prefix = 0
        max_len = 0
        first_occurrence = {0: -1}

        for i, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix])
            else:
                first_occurrence[prefix] = i

        return max_len
        