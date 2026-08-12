# Last updated: 8/12/2026, 11:48:39 AM
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            # If arr[mid] is less than arr[mid+1], it means we are on the increasing
            # part of the mountain. The peak must be to the right of mid.
            # We can discard mid and everything to its left.
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            # If arr[mid] is greater than arr[mid+1], it means we are either
            # at the peak or on the decreasing part of the mountain.
            # The peak could be mid, or it could be to the left of mid.
            # We cannot discard mid, so we set the right boundary to mid.
            else: # arr[mid] > arr[mid+1]
                right = mid
        
        # When the loop terminates, left == right, and this index is the peak element.
        return left