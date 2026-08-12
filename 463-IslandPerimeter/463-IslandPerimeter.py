# Last updated: 8/12/2026, 11:49:36 AM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        # Define directions for neighbors (up, down, left, right)
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # If it's a land cell
                    # Each land cell initially contributes 4 to the perimeter
                    perimeter += 4
                    
                    # Check its neighbors
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]

                        # If a neighbor is within grid bounds and is also land,
                        # then this side is shared and not part of the perimeter.
                        # So, subtract 1 from the perimeter for this shared edge.
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            perimeter -= 1
        
        return perimeter