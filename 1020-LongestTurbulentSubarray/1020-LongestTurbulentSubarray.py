# Last updated: 8/12/2026, 11:48:28 AM
class Solution:
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        
        up = down = 1
        ans = 1
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
                up = 1
            else:
                up = down = 1
            
            ans = max(ans, up, down)
        
        return ans