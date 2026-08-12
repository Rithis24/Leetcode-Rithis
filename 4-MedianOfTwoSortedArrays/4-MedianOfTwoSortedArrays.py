# Last updated: 8/12/2026, 11:52:44 AM
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the shorter array to optimize binary search range.
        # The binary search will be performed on the shorter array.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        
        # 'i' is the partition point for nums1 (number of elements taken from nums1 for the left partition)
        # 'j' is the partition point for nums2 (number of elements taken from nums2 for the left partition)
        # We need to find 'i' such that:
        # 1. Number of elements in the left combined partition equals total_left_half_elements.
        #    i + j = (m + n + 1) // 2
        # 2. max(elements in left_part) <= min(elements in right_part).
        #    This translates to:
        #    nums1[i-1] <= nums2[j] (if i > 0 and j < n)
        #    nums2[j-1] <= nums1[i] (if j > 0 and i < m)

        # The range for binary search on 'i' (partition in nums1)
        low = 0
        high = m # 'i' can range from 0 to m (inclusive)

        # total_left_half_elements represents the desired number of elements
        # in the combined left partition.
        # Using (m + n + 1) // 2 ensures that:
        # - If (m+n) is odd, total_left_half_elements is (m+n)/2 + 1 (e.g., for 3 elements, 2 in left).
        #   The median will be max(L1, L2).
        # - If (m+n) is even, total_left_half_elements is (m+n)/2 (e.g., for 4 elements, 2 in left).
        #   The median will be (max(L1, L2) + min(R1, R2)) / 2.0.
        total_left_half_elements = (m + n + 1) // 2 

        while low <= high:
            i = (low + high) // 2 # Current partition point for nums1
            j = total_left_half_elements - i # Corresponding partition point for nums2

            # Define boundary values, using -infinity and +infinity for edge cases.
            # L1: Element immediately to the left of partition 'i' in nums1.
            # R1: Element immediately to the right of partition 'i' in nums1.
            # L2: Element immediately to the left of partition 'j' in nums2.
            # R2: Element immediately to the right of partition 'j' in nums2.

            L1 = float('-inf') if i == 0 else nums1[i-1]
            R1 = float('inf') if i == m else nums1[i]
            L2 = float('-inf') if j == 0 else nums2[j-1]
            R2 = float('inf') if j == n else nums2[j]

            # Check if we have found the correct partition
            if L1 <= R2 and L2 <= R1:
                # The partitions are correct.
                # Now, calculate the median based on total length parity.
                if (m + n) % 2 == 1: # Total length is odd
                    # The median is the largest element in the left partition.
                    return float(max(L1, L2))
                else: # Total length is even
                    # The median is the average of the largest element in the left partition
                    # and the smallest element in the right partition.
                    return (float(max(L1, L2)) + float(min(R1, R2))) / 2.0
            elif L1 > R2:
                # L1 is too large, meaning we took too many elements from nums1's left partition.
                # We need to move the partition 'i' to the left.
                high = i - 1
            else: # L2 > R1
                # L2 is too large, meaning we took too many elements from nums2's left partition.
                # This implies we took too few from nums1's left partition.
                # We need to move the partition 'i' to the right.
                low = i + 1
        
        # This part should theoretically not be reached as a valid partition always exists
        # given the problem constraints (m+n >= 1).
        return 0.0