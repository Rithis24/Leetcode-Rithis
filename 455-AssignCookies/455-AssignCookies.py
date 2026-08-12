# Last updated: 8/12/2026, 11:49:38 AM
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        child_idx = 0
        cookie_idx = 0
        content_children = 0

        while child_idx < len(g) and cookie_idx < len(s):
            if s[cookie_idx] >= g[child_idx]:
                # This cookie can satisfy this child
                content_children += 1
                child_idx += 1  # Move to the next child
                cookie_idx += 1 # Move to the next cookie
            else:
                # This cookie is too small for the current child, try a larger cookie
                cookie_idx += 1
        
        return content_children