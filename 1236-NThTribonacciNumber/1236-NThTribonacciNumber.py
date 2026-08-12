# Last updated: 8/12/2026, 11:48:13 AM
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        # Initialize the first three Tribonacci numbers
        t0 = 0
        t1 = 1
        t2 = 1

        # Iterate from n=3 up to the target n
        for i in range(3, n + 1):
            # Calculate the current Tribonacci number
            tn = t0 + t1 + t2
            # Shift the values for the next iteration
            t0 = t1
            t1 = t2
            t2 = tn
        
        # t2 now holds the value of Tn
        return t2