// Last updated: 8/12/2026, 11:46:24 AM
class Solution {
    public int maxDistance(String moves) {
        int x = 0, y = 0, blanks = 0;
        
        for (char c : moves.toCharArray()) {
            switch (c) {
                case 'U' -> y++;
                case 'D' -> y--;
                case 'L' -> x--;
                case 'R' -> x++;
                case '_' -> blanks++;
            }
        }
        
        return Math.abs(x) + Math.abs(y) + blanks;
    }
}