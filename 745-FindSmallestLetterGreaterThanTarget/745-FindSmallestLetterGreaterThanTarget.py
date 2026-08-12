# Last updated: 8/12/2026, 11:48:45 AM
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        
        # Initialize binary search pointers.
        # 'low' represents the start of the search range.
        # 'high' represents the end of the search range (exclusive, so it can be 'n').
        low = 0
        high = n 
        
        # Perform binary search to find the smallest character strictly greater than target.
        # This loop is designed to find the "insertion point" for 'target' if we were to maintain
        # the sorted order, specifically, the index of the first element greater than target.
        while low < high:
            mid = low + (high - low) // 2
            
            if letters[mid] <= target:
                # The current character is not greater than target, or is equal to target.
                # We need to look in the right half for a greater character.
                low = mid + 1
            else:
                # The current character is greater than target. This is a potential answer.
                # We try to find an even smaller one in the left half (including mid).
                high = mid
        
        # After the loop, 'low' will be the index of the smallest character
        # lexicographically greater than target.
        #
        # If all characters in 'letters' are less than or equal to 'target'
        # (e.g., letters = ["x", "y"], target = "z"), then 'low' will be 'n' (len(letters)).
        # In this scenario, the problem states we should return the first character of 'letters'.
        #
        # The modulo operator 'low % n' elegantly handles both cases:
        # - If 'low' is a valid index (0 to n-1), then low % n == low.
        # - If 'low' is 'n', then n % n == 0, returning letters[0].
        return letters[low % n]