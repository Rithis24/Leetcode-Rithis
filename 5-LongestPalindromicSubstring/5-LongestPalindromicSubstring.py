# Last updated: 8/12/2026, 11:52:42 AM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 1:
            return ""

        start = 0
        maxLength = 1

        def expandAroundCenter(left: int, right: int) -> int:
            nonlocal s, n
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(n):
            len1 = expandAroundCenter(i, i)
            if len1 > maxLength:
                maxLength = len1
                start = i - (len1 - 1) // 2

            len2 = expandAroundCenter(i, i + 1)
            if len2 > maxLength:
                maxLength = len2
                start = i - len2 // 2 + 1
        
        return s[start : start + maxLength]