# Last updated: 8/12/2026, 11:49:45 AM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False

        left, right = 1, num

        while left <= right:
            mid = left + (right - left) // 2
            
            # Using mid_square for clarity and to avoid recomputing
            # Python integers handle arbitrary size, so no overflow for mid * mid
            mid_square = mid * mid

            if mid_square == num:
                return True
            elif mid_square < num:
                left = mid + 1
            else: # mid_square > num
                right = mid - 1
        
        return False