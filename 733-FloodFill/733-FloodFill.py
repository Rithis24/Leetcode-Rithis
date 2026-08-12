# Last updated: 8/12/2026, 11:48:47 AM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]

        # If the starting pixel already has the target color, no fill is needed.
        # This also prevents infinite recursion if original_color == color.
        if original_color == color:
            return image

        # DFS approach
        def dfs(r, c):
            # Check boundary conditions and if the pixel has the original color
            if not (0 <= r < m and 0 <= c < n and image[r][c] == original_color):
                return

            # Change the color of the current pixel
            image[r][c] = color

            # Recursively call DFS for all four adjacent pixels
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Start the flood fill from the given (sr, sc)
        dfs(sr, sc)

        return image