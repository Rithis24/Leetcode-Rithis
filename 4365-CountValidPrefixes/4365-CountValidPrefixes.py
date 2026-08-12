# Last updated: 8/12/2026, 11:46:20 AM
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        z=0
        o=0
        a=0
        for c in s:
            if c=='0':
                z+=1
            else:
                o+=1
            if abs(z-o)<=1:
                a+=1
        return a