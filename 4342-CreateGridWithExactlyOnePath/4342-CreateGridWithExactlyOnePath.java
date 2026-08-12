// Last updated: 8/12/2026, 11:46:21 AM
class Solution {
    public String[] createGrid(int m, int n) {
        char[][] grid = new char[m][n];
        
        // Fill everything with obstacles first
        for (int i = 0; i < m; i++) {
            Arrays.fill(grid[i], '#');
        }
        
        // First row: all free (forces rightward movement)
        for (int j = 0; j < n; j++) {
            grid[0][j] = '.';
        }
        
        // Last column: all free (forces downward movement)
        for (int i = 0; i < m; i++) {
            grid[i][n - 1] = '.';
        }
        
        String[] result = new String[m];
        for (int i = 0; i < m; i++) {
            result[i] = new String(grid[i]);
        }
        
        return result;
    }
}